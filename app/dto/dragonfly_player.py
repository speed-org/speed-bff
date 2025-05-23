from dataclasses import dataclass


@dataclass
class DragonflyPlayerDTO:
    id: str
    sid: str
    status: str
    wait_time: int
