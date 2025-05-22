from dataclasses import dataclass


@dataclass
class Card:
    id: str
    number: int
    symbol: str
