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
