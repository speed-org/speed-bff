from typing import Optional
from app import r
from app.utils.dragonfly_helpers import create_player_key, decode_bytes
from app.utils.constants import DragonflyMatchingField


class DragonflyPlayerRepository:

    @staticmethod
    def get_socket_id(player_id: str) -> Optional[str]:
        """
        Retrieves WebSocket ID from Dragonfly Player database.
        """
        player_key = create_player_key(player_id)
        socket_id = r.hget(player_key, DragonflyMatchingField.WEBSOCKET_ID.value)
        decoded_id = decode_bytes(socket_id)

        return decoded_id if isinstance(decoded_id, str) else None
