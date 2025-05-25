from typing import Optional, Any
from app import r
from app.utils.dragonfly_helpers import create_player_key
from app.utils.constants import DragonflyPlayerField
import time
from app.dto.dragonfly_player import DragonflyPlayerDTO
from app.utils.constants import DragonflyPlayerField as fields


class DragonflyPlayerRepository:
    @staticmethod
    def get_socket_id(player_id: str) -> Optional[str]:
        """
        Retrieves WebSocket ID from Dragonfly Player database.
        """
        player_key = create_player_key(player_id)
        socket_id: Optional[str] = r.hget(
            player_key, DragonflyPlayerField.WEBSOCKET_ID.value
        )

        return socket_id

    @staticmethod
    def update_player_status(player_id: str, status: str) -> Optional[str]:
        """
        Updates player status to desired status.
        """
        player_key = create_player_key(player_id)
        r.hset(player_key, DragonflyPlayerField.STATUS.value, status)

        new_status: Optional[str] = r.hget(
            player_key, DragonflyPlayerField.STATUS.value
        )

        return new_status

    @staticmethod
    def update_player_wait_time(player_id: str) -> Optional[int]:
        """
        Updates player wait_time to current time.
        """
        player_key = create_player_key(player_id)
        r.hset(player_key, DragonflyPlayerField.WAIT_TIME.value, int(time.time()))

        new_wait_time = r.hget(player_key, DragonflyPlayerField.WAIT_TIME.value)

        return int(new_wait_time) if new_wait_time else None

    @staticmethod
    def save_player(player: DragonflyPlayerDTO) -> dict[str, Any]:
        player_key = create_player_key(player.id)

        # Register ws_id, status and wait_time
        r.hset(
            player_key,
            mapping={
                fields.WS_ID.value: player.sid,
                fields.STATUS.value: player.status,
                fields.WAIT_TIME.value: player.wait_time,
            },
        )
        new_player: dict = r.hgetall(player_key)

        return new_player
