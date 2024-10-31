from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from twilio.rest import Client
from .config import Config

# Initialize extensions
db = SQLAlchemy()
migrate = Migrate()
twilio_client = None

def create_app():
    app = Flask(__name__)
    
    # Load configuration
    app.config.from_object(Config)

    # Initialize extensions
    db.init_app(app)
    migrate.init_app(app, db)
    
    from app.models import Alert

    # Initialize Twilio client
    global twilio_client
    twilio_client = Client(app.config['TWILIO_ACCOUNT_SID'], app.config['TWILIO_AUTH_TOKEN'])

    # Register routes
    from .routes import main as main_blueprint
    app.register_blueprint(main_blueprint)

    return app
