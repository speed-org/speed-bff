from app.utils.constants import DragonflyNamespace
from app import redis_client as r
from app.dto.dragonfly_player import DragonflyPlayer
from typing import Union

# Using this class to directly interact with Dragonfly about Matching System 

class DragonflyMatchSystemRepository:

    @staticmethod
    def add_user_to_waitroom(player: DragonflyPlayer) -> Union[None, str]:
        """
        Add a user to the waiting room.
        """
        key = f"{DragonflyNamespace.PLAYER.value}{player.id}"
        value = player.status
        r.hset(key, value)

        return r.hget(key)
    
    