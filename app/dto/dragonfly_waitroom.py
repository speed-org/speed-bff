from dataclasses import dataclass


@dataclass
class DragonflyWaitroomDTO:
    id: str
    player1_id: str
    player2_id: str
    player1_accepted: bool
    player2_accepted: bool
