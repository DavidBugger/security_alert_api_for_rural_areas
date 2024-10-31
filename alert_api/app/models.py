from . import db
from datetime import datetime

class Alert(db.Model):
    __tablename__ = 'alerts'
    
    id = db.Column(db.Integer, primary_key=True)
    description = db.Column(db.String(255), nullable=False)
    latitude = db.Column(db.Float, nullable=False)
    longitude = db.Column(db.Float, nullable=False)
    timestamp = db.Column(db.DateTime, default=datetime.utcnow)
    status = db.Column(db.String(50), nullable=False, default='pending')  

    def __repr__(self):
        return f"<Alert {self.description} at {self.latitude}, {self.longitude}>"
