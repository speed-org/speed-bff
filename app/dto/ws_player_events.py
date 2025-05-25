from dataclasses import dataclass, field
from typing import Optional
from app.models.event import EventBase
from app.utils.constants import WS_EVENT


# PlayerNotSavedToDrangonfly
@dataclass
class PlayerNotSavedToDrangonflyPayloadDTO:
    player_id: str
    message: str


@dataclass
class PlayerNotSavedToDragonflyEventDTO(
    EventBase[PlayerNotSavedToDrangonflyPayloadDTO]
):
    _type: str = field(default=WS_EVENT.PLAYER_NOT_SAVED_TO_DRAGONFLY.value)
    payload: PlayerNotSavedToDrangonflyPayloadDTO


# NoPlayerIdOrSid
@dataclass
class NoPlayerIdOrSidPayloadDTO:
    player_id: Optional[str]
    sid: Optional[str]
    message: str


@dataclass
class NoPlayerIdOrSidEventDTO(EventBase[NoPlayerIdOrSidPayloadDTO]):
    _type: str = field(default=WS_EVENT.NO_PLAYER_ID_OR_SID.value)
    payload: NoPlayerIdOrSidPayloadDTO
