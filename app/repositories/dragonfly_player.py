from typing import Optional
from app import r
from app.utils.dragonfly_helpers import create_player_key, decode_bytes
from app.utils.constants import DragonflyMatchingField
import time


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

    @staticmethod
    def update_player_status(player_id: str, status: str) -> str:
        """
        Updates player status to desired status.
        """
        player_key = create_player_key(player_id)
        r.hset(player_key, DragonflyMatchingField.STATUS.value, status)

        new_status = decode_bytes(
            r.hget(player_key, DragonflyMatchingField.STATUS.value)
        )

        return str(new_status)

    @staticmethod
    def update_player_wait_time(player_id: str) -> int:
        """
        Updates player wait_time to current time.
        """
        player_key = create_player_key(player_id)
        r.hset(player_key, DragonflyMatchingField.WAIT_TIME.value, int(time.time()))

        new_wait_time = decode_bytes(
            r.hget(player_key, DragonflyMatchingField.WAIT_TIME.value)
        )

        return int(new_wait_time)
