from app.utils.constants import WS_EVENT
from .player import save_player_to_dragonfly_on_connect
from flask_socketio import SocketIO


def register_handlers(socketio: SocketIO) -> None:
    socketio.on_event(WS_EVENT.ON_CONNECT, save_player_to_dragonfly_on_connect)
