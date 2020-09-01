from flask import Flask
from modules.root.view import root_view
from core.database import init_db
from dotenv import load_dotenv
import os

load_dotenv('.env')


def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = os.environ.get('SECRET_KEY')

    app.config.from_pyfile('settings.py')

    init_db()

    app.register_blueprint(root_view)

    return app
