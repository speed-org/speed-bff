from enum import Enum


class TableName(Enum):
    PLAYER = "player"
    GAME_STATE = "game_state"


class DragonflyNamespace(Enum):
    PLAYER = "player:"


class DragonflyPlayerStatus(Enum):
    CONNECTED = "connected"
    WAITING = "waiting"
    PENDING = "pending"
    PLAYING = "playing"


class DragonflyPlayerField(Enum):
    WS_ID = "ws_id"
    STATUS = "status"
    WAIT_TIME = "wait_time"


class WS_EVENT(Enum):
    ON_CONNECT = ("connect",)
    ON_DISCONNECT = "disconnect"
    ON_RECONNECT = "reconnect"
    PLAYER_NOT_SAVED_TO_DRAGONFLY = "player-not-saved-to-dragonfly"
    NO_PLAYER_ID_OR_SID = "no-player-id-or-sid"


class WS_EVENT_HANDLER_FIELD(Enum):
    USER_ID = "user_id"
    SID = "sid"


DRAGONFLY_PLAYER_DEFAULT_WAIT_TIME = 0
UTF_8 = "utf-8"
