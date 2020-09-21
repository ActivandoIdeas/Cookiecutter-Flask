"""
Initialized example
"""

from flask import Flask
from dotenv import load_dotenv
from app.connection.db_instance import db
from flask_migrate import Migrate
from os import environ

# Main modules
from modules.example.view import example_view

# Custom configuration environments
from .config import config

# Load env variables
load_dotenv(".env")


def create_app(environment):
    """Basic modularized example configuration"""
    application = Flask(__name__)

    application.config.from_object(environment)

    db.init_app(application)
    with application.app_context():
        application.register_blueprint(example_view)
        Migrate(application, db)

    return application


# Create example
env = config[environ.get('environment_execution')]
app = create_app(env)
