import logging
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_cors import CORS
from app.config import Config
from app.services.dragonfly import DragonflyService
import redis
from flask_socketio import SocketIO


db = SQLAlchemy()
migrate = Migrate()
socketio = SocketIO()
logger = logging.getLogger(__name__)
r = redis.from_url(Config.REDIS_URL, decode_responses=True)


def create_app(config: Config) -> Flask:
    """
    Create and configure the Flask application.
    """
    from app.event_handlers import register_handlers

    app = Flask(__name__)
    app.config.from_object(config)

    # Configure CORS using the allowed origins from config
    CORS(app, resources={r"/*": {"origins": config.ALLOWED_ORIGINS}})
    DragonflyService.init_player_index(r)

    db.init_app(app)
    migrate.init_app(app, db)
    socketio.init_app(app, cors_allowed_origins=config.ALLOWED_ORIGINS)
    register_handlers(socketio)

    return app
