import logging
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_cors import CORS
from app.config import Config
from flask_redis import FlaskRedis

db = SQLAlchemy()
migrate = Migrate()
log = logging.getLogger(__name__)
redis_client = FlaskRedis()

def create_app(config: Config):
    """
    Create and configure the Flask application.
    """

    app = Flask(__name__)
    app.config.from_object(config)

    # TODO: Configure CORS - allow all origins in development
    CORS(app, resources={r"/*": {"origins": "*"}})

    db.init_app(app)
    redis_client.init_app(app)

    return app