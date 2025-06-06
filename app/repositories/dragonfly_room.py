from app.utils.dragonfly_helpers import (
    generate_room_key,
)
from app import r
from app.dto.dragonfly_room import DragonflyRoomDTO
from app.utils.constants import DragonflyRoomField
from typing import Any, Optional


class DragonflyRoomRepository:
    @staticmethod
    def generate_room(room_dto: DragonflyRoomDTO) -> Optional[dict[str, str]]:
        """
        Generates websocket room key and uploads waitroom info to database.
        """
        room_key = generate_room_key(room_dto.id)

        # TODO: validate the state is not None
        r.hset(
            room_key,
            mapping={
                DragonflyRoomField.PLAYER1_ID.value: room_dto.player1_id,
                DragonflyRoomField.PLAYER2_ID.value: room_dto.player2_id,
                DragonflyRoomField.GAME_STATE.value: room_dto.gamestate,
            },
        )

        new_room: dict[str, Any] = r.hgetall(room_key)

        return new_room if isinstance(new_room, dict) else None
