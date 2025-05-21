from app.utils.constants import UTF_8, DragonflyNamespace


def decode_bytes(bytes) -> any:
    return bytes.decode(UTF_8) if bytes else None

def create_player_key(player_id:str):
    return f"{DragonflyNamespace.PLAYER.value}{player_id}"

def get_player_id_from_key(key:str):
    return key.split(":")[1]
