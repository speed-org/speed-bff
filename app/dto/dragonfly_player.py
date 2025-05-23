from dataclasses import dataclass


@dataclass
class DragonflyPlayer:
    id: str
    sid: str
    status: str
    wait_time: int
