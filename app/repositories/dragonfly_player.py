from app.dto.dragonfly_player import DragonflyPlayerDTO
from app.utils.dragonfly_helpers import create_player_key
from app.utils.constants import DragonflyPlayerField as fields
from app import r
from typing import Any


class DragonflyPlayerRepository:
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
