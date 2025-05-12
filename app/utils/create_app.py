from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_restx import Api
from flask_cors import CORS


def create_app():
    """
    Create and configure the Flask application.
    """

    app = Flask(__name__)
    CORS(app, supports_credentials=True)
    #app.config.from_object('config.Config')


    return app