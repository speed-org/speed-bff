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

class DragonflyMatchingField(Enum):
    STATUS = "status"
    WAIT_TIME = "wait_time"


UTF_8 = "utf-8"
