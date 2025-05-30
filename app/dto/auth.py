from dataclasses import dataclass
from .response_dto import ResponseDTO


@dataclass
class RegisterPlayerPayloadDTO:
    name: str
    lastName: str
    email: str
    firebaseId: str
    refreshToken: str


@dataclass
class RegisterPlayerResponseDTO(ResponseDTO):
    new_player_id: str


@dataclass
class LogInPlayerPayloadDTO:
    firebaseId: str


@dataclass
class LogInPlayerResponseDTO(ResponseDTO):
    id: str
