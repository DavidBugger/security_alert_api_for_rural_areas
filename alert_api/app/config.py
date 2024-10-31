import os

class Config:
    # SQLALCHEMY_DATABASE_URI = os.getenv('DATABASE_URL') or 'sqlite:///site.db'
    SQLALCHEMY_DATABASE_URI = os.getenv('SQLALCHEMY_DATABASE_URI') 
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    TWILIO_ACCOUNT_SID = os.getenv('TWILIO_ACCOUNT_SID')
    TWILIO_AUTH_TOKEN = os.getenv('TWILIO_AUTH_TOKEN')
    


