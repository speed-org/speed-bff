from app.utils.constants import UTF_8

def decode_bytes(bytes) -> any:
    return bytes.decode(UTF_8) if bytes else None