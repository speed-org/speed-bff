from dataclasses import dataclass
from typing import Optional
from app.dto.gamestate import GameStateDTO


@dataclass
class DragonflyRoomDTO:
    id: str
    player1_id: str
    player2_id: str
    gamestate: Optional[GameStateDTO]
    is_active: bool
