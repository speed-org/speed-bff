from app.utils.constants import DragonflyNamespace


def create_player_key(player_id: str) -> str:
    return f"{DragonflyNamespace.PLAYER.value}{player_id}"


def get_player_id_from_key(key: str) -> str:
    return key.split(":")[1]
