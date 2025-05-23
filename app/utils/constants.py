from enum import Enum


class TableName(Enum):
    PLAYER = "player"
    GAME_STATE = "game_state"


class DragonflyNamespace(Enum):
    PLAYER = "player:"
    ROOM = "room:"
    WAITROOM = "waitroom:"


class DragonflyMatchingStatus(Enum):
    CONNECTED = "connecting"
    WAITING = "waiting"
    PENDING = "pending"
    PLAYING = "playing"


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


class DragonflyWaitroomField(Enum):
    PLAYER1_ID = "player1_id"
    PLAYER2_ID = "player2_id"
    PLAYER1_ACCEPTED = "player1_accepted"
    PLAYER2_ACCEPTED = "player2_accepted"


UTF_8 = "utf-8"
NONE_STRING = "None"
