from flask import Blueprint, request, jsonify
from .models import Alert
from . import db, twilio_client
import logging
main = Blueprint('main', __name__)

# Create a new alert
@main.route('/alert', methods=['POST'])
def create_alert():
    data = request.get_json()
    # Retrieve and validate data fields
    description = data.get('description')
    latitude = data.get('latitude')
    longitude = data.get('longitude')
    timestamp = data.get('timestamp')
    if not description or not latitude or not longitude:
        return jsonify({"error": "Missing required fields"}), 400
    
    # Create and save new alert
    new_alert = Alert(description=description, latitude=latitude, longitude=longitude, timestamp=timestamp)
    db.session.add(new_alert)
    db.session.commit()
    
    # logging for debugging purposes
    logging.basicConfig(filename='app.log', level=logging.DEBUG)
    #Sending SMS alert
    try:
        twilio_client.messages.create(
            body=f"Security Alert: {description} at {latitude}, {longitude}",
            from_='+15097923288',
            to='+2348107701730'
        )
    except Exception as e:
        
        print(f"Twilio error: {e}")
        return jsonify({"error": "Alert created but SMS failed"}), 500

    return jsonify({"status": "Alert created successfully", "alert_id": new_alert.id}), 201

# Retrieve alerts by location
@main.route('/alerts', methods=['GET'])
def get_alerts():
    # Get latitude and longitude from query parameters
    latitude = request.args.get('latitude')
    longitude = request.args.get('longitude')
    
    if latitude is None or longitude is None:
        return jsonify({"error": "Latitude and longitude are required"}), 400
    
    try:
        latitude = float(latitude)
        longitude = float(longitude)
    except ValueError:
        return jsonify({"error": "Latitude and longitude must be numeric"}), 400
    # Query the database for matching alerts
    alerts = Alert.query.filter_by(latitude=latitude, longitude=longitude).all()
    # If no alerts are found, return a message
    if not alerts:
        return jsonify({"message": "No alerts found for this location"}), 404
    # Return alerts in JSON format
    return jsonify([{
        'description': alert.description,
        'latitude': alert.latitude,
        'longitude': alert.longitude,
        'timestamp': alert.timestamp.strftime('%a, %d %b %Y %H:%M:%S GMT')  
    } for alert in alerts])


# Get stats of alerts
@main.route('/alerts/stats', methods=['GET'])
def get_stats():
    total_alerts = Alert.query.count()
    recent_alerts = Alert.query.order_by(Alert.timestamp.desc()).limit(10).all()
    
    return jsonify({
        "total_alerts": total_alerts,
        "recent_alerts": [{
            'description': alert.description,
            'timestamp': alert.timestamp
        } for alert in recent_alerts]
    })
