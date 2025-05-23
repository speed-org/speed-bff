from enum import Enum


class TableName(Enum):
    PLAYER = "player"
    GAME_STATE = "game_state"


class DragonflyNamespace(Enum):
    PLAYER = "player:"
    ROOM = "room:"


class DragonflyMatchingStatus(Enum):
    WAITING = "waiting"
    PENDING = "pending"
    ACTIVE = "active"


class DragonflyMatchingField(Enum):
    STATUS = "status"
    WAIT_TIME = "wait_time"
    WEBSOCKET_ID = "websocket_id"


class WsRoomEvent(Enum):
    JOIN = "join_room"


class DragonflyRoomField(Enum):
    PLAYER1_ID = "player1_id"
    PLAYER2_ID = "player2_id"
    GAME_STATE = "game_state"
    IS_ACTIVE = "is_active"


UTF_8 = "utf-8"
NONE_STRING = "None"
