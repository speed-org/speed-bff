from typing import Any
from dataclasses import is_dataclass, asdict


class ResponseDTO:
    def __init__(self, **kwargs: Any) -> None:
        self.__dict__.update(kwargs)
    
    def to_dict(self) -> dict:
        """Convert to dictionary, handling both regular attributes and dataclass fields."""
        # For dataclass subclasses, use asdict; otherwise use __dict__
        return asdict(self) if is_dataclass(self) else self.__dict__.copy()