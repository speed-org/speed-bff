from dataclasses import dataclass


@dataclass
class DragonflyPlayer:
    id: str
    status: str
    wait_time: int
