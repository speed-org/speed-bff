from app.utils.constants import DragonflyNamespace, DRAGONFLY_STATUS_FIELD
from app import redis_client as r
from app.dto.dragonfly_player import DragonflyPlayer
from typing import Union
from app.utils.dragonfly_helpers import decode_bytes

# Using this class to directly interact with Dragonfly about Matching System 

class DragonflyMatchSystemRepository:

    @staticmethod
    def add_user_to_waitroom(player: DragonflyPlayer) -> Union[None, str]:
        """
        Add a user to the waiting room.
        """
        player_key = f"{DragonflyNamespace.PLAYER.value}{player.id}"
        field = DRAGONFLY_STATUS_FIELD
        value = player.status
        r.hset(player_key, field, value)

        result = decode_bytes(r.hget(player_key, field))
        return result
