from flask import Flask
from modules.{{cookiecutter.project_slug}}.view import {{cookiecutter.project_slug}}_view
from dotenv import load_dotenv
from .extensions import db
from flask_migrate import Migrate

load_dotenv('.env')


def create_app():
    app = Flask(__name__)

    app.config.from_pyfile('settings.py')
    db.init_app(app)
    with app.app_context():
        app.register_blueprint({{cookiecutter.project_slug}}_view)
        Migrate(app, db)

    return app
