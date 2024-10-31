# Security Alert API for Rural Areas

## Overview
The Security Alert API is designed to aggregate and broadcast real-time security alerts in rural areas affected by insecurity, especially in regions like Plateau State. It provides a simple interface for reporting security incidents, notifying local authorities and residents, and analyzing trends over time.

This API integrates with the Twilio API to send SMS alerts to users based on geolocation. It's built using Flask and uses PostgreSQL for storing data.

## Features
- Report Security Incidents: Farmers and authorities can post alerts in real-time.
- Retrieve Alerts by Location: Users can filter alerts based on latitude and longitude.
- Statistics and Trends: Analyze security patterns over time with attack frequency and location-based statistics.
- Twilio SMS Integration: Automatically notify subscribed users of security incidents in their area.

## Endpoints

### 1. Create a New Alert
POST `/alert`
- Description: Allows users to report a new security incident in their location.
- Payload Example:
  ```json
  {
    "description": "Armed attack reported in the area.",
    "latitude": 9.3082,
    "longitude": 8.7118,
    "timestamp": "2024-10-10T10:00:00"
  }

  {
  "status": "Alert created successfully",
  "alert_id": 1
}

2. Retrieve Alerts by Location
GET /alerts

Query Parameters: latitude, longitude, radius (optional).

GET /alerts?latitude=9.3082&longitude=8.7118&radius=10

[
  {
    "alert_id": 1,
    "description": "Armed attack reported in the area.",
    "latitude": 9.3082,
    "longitude": 8.7118,
    "timestamp": "2024-10-10T10:00:00"
  },
  ...
]

3. Retrieve Security Stats
GET /alerts/stats

Description: Provides statistical analysis of security alerts (e.g., number of incidents over time).
Response Example:

{
  "total_alerts": 50,
  "alerts_last_7_days": 5,
  "alerts_by_region": {
    "region_1": 20,
    "region_2": 15
  }
}
Tech Stack
Python (Flask)
PostgreSQL for data persistence.
Twilio API for SMS alerts.
SQLAlchemy for ORM.
Alembic for database migrations.
Docker for containerization.

Installation
1. Clone the Repository
git clone https://github.com/your-username/security-alert-api.git
cd security-alert-api

2. Create and Activate Virtual Environment
python3 -m venv venv
source venv/bin/activate for macos
venv\Scripts\activate for windows 

3. Install Dependencies
pip install -r requirements.txt
4. Set Up Environment Variables Create a .env file with the following:
FLASK_ENV=development
TWILIO_ACCOUNT_SID=your_twilio_sid
TWILIO_AUTH_TOKEN=your_twilio_auth_token
DATABASE_URL=postgresql://user:password@localhost:5432/security_alerts_db
5. Run Database Migrations
flask db upgrade
6. Start the Application
flask run

Running Tests
To run the unit tests:
Running Tests
To run the unit tests:

Deployment with Docker
To build and run the Docker container:
docker build -t security-alert-api .
docker run -p 5000:5000 security-alert-api


Running migrations using Flask
flask db init
flask db migrate -m "Initial migration."
flask db upgrade

#Below are the links shows demonstration on postman and the receiving message on my phone
#Link 1
https://drive.google.com/file/d/1zAVX-rnot7iWn00D84Bl8WbPH-Mm25tu/view?usp=sharing
#Link 2 
https://drive.google.com/file/d/1c3alSaZl7ZvKbnt8aq7ZTz0C9Dqn1HWH/view?usp=sharing
