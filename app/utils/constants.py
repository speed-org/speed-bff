from enum import Enum

class TableName(Enum):
    PLAYER = 'player'
    GAME_STATE = 'game_state'

class DragonflyNamespace(Enum):
    PLAYER = 'player:'

class DragonflyMatchingStatus(Enum):
    WAITING = 'waiting'
    PENDING = 'pending'
    ACTIVE = 'active'

UTF_8 = "utf-8"
DRAGONFLY_STATUS_FIELD = "status"