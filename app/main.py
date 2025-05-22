from app.api import api
from app import create_app
from app.config import Config
from app import socketio
import logging

# Configure logging
logging.basicConfig(
    level=logging.INFO, format="%(asctime)s - %(name)s - %(levelname)s - %(message)s"
)

config = Config()
app = create_app(config)
api.init_app(app)

if __name__ == "__main__":
    socketio.run(app, debug=True)
