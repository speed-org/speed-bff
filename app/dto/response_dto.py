from dataclasses import dataclass


class ResponseDTO:
    def __init__(self, **kwargs) -> None:
        for key, value in kwargs.items():
            setattr(self, key, value)