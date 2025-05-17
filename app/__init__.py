import logging
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_cors import CORS
from app.config import Config

db = SQLAlchemy()
migrate = Migrate()
log = logging.getLogger(__name__)


def create_app(config: Config):
    """
    Create and configure the Flask application.
    """

    app = Flask(__name__)
    app.config.from_object(config)

    # Configure CORS
    allowed_origins = [origin.strip() for origin in Config.ALLOWED_ORIGINS.split(",")]
    CORS(app, resources={r"/*": {"origins": allowed_origins}})

    db.init_app(app)

    return app