from flask import Flask
from modules.root.view import root_view
from dotenv import load_dotenv
from .extensions import db
from flask_migrate import Migrate

load_dotenv('.env')


def create_app():
    app = Flask(__name__)

    app.config.from_pyfile('settings.py')
    db.init_app(app)
    with app.app_context():
        app.register_blueprint(root_view)
        Migrate(app, db)

    return app
