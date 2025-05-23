from dataclasses import dataclass, field
from typing import Generic, TypeVar


T = TypeVar("T")


@dataclass
class EventBase(Generic[T]):
    payload: T
    _type: str = field(init=False)
