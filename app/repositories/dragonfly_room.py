from app.utils.dragonfly_helpers import (
    decode_bytes,
    generate_room_key,
)
from app import r
from app.dto.dragonfly_room import DragonflyRoomDTO
from app.utils.constants import DragonflyRoomField
from typing import Optional


class DragonflyRoomRepository:
    @staticmethod
    def generate_room(room_dto: DragonflyRoomDTO) -> Optional[dict[str, str]]:
        """
        Generates websocket room and joins two matched players.
        """
        room_key = generate_room_key(room_dto.id)

        # TODO: validate the state is not None
        r.hset(
            room_key,
            mapping={
                DragonflyRoomField.PLAYER1_ID.value: room_dto.player1_id,
                DragonflyRoomField.PLAYER2_ID.value: room_dto.player2_id,
                DragonflyRoomField.GAME_STATE.value: room_dto.gamestate,
                DragonflyRoomField.IS_ACTIVE.value: room_dto.is_active,
            },
        )

        new_room = decode_bytes(r.hgetall(room_key))

        return new_room if isinstance(new_room, dict) else None
