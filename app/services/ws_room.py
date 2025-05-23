from app import socketio
from app.utils.constants import WsRoomEvent


class WsRoomService:

    @staticmethod
    def join_room(socket_ids: list[str], room_key: str) -> None:
        """
        Joins two players into a WebSocket room.
        """
        for socket_id in socket_ids:
            socketio.emit(WsRoomEvent.JOIN.value, room_key, to=socket_id)
