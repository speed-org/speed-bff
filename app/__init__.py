import logging
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_cors import CORS
from app.config import Config
from app.services.dragonfly import DragonflyService
from app.config import Config
import redis



db = SQLAlchemy()
migrate = Migrate()
log = logging.getLogger(__name__)
r = redis.from_url(Config.REDIS_URL)


def create_app(config: Config):
    """
    Create and configure the Flask application.
    """

    app = Flask(__name__)
    app.config.from_object(config)

    # TODO: Configure CORS - allow all origins in development
    CORS(app, resources={r"/*": {"origins": "*"}})
    DragonflyService.init_player_index(r)

    db.init_app(app)

    return app