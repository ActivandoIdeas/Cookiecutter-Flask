from os import environ

SECRET_KEY = environ.get('SECRET_KEY')
SQLALCHEMY_DATABASE_URI = f"postgresql://{environ.get('DB_USER')}:{environ.get('DB_PASSWORD')}@{environ.get('DB_HOST')}:{environ.get('DB_PORT')}/{environ.get('DB_NAME')}"