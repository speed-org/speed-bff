from app.utils.constants import DragonflyNamespace
import uuid


def create_player_key(player_id: str) -> str:
    return f"{DragonflyNamespace.PLAYER.value}{player_id}"


def get_id_from_key(key: str) -> str:
    return key.split(":")[1]


def generate_room_key(id: str) -> str:
    return f"{DragonflyNamespace.ROOM.value}{id}"


def generate_waitroom_key(id: str) -> str:
    return f"{DragonflyNamespace.WAITROOM.value}{id}"


def generate_random_id() -> str:
    return str(uuid.uuid4())
