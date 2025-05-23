from app.dto.ws_player_events import (
    PlayerNotSavedToDragonflyEventDTO,
    PlayerNotSavedToDrangonflyPayloadDTO,
    NoPlayerIdOrSidEventDTO,
    NoPlayerIdOrSidPayloadDTO,
)
from app.repositories.dragonfly_player import DragonflyPlayerRepository
from app.dto.dragonfly_player import DragonflyPlayerDTO
from app.services.ws_player import WsPlayerService
from app.utils.constants import (
    DragonflyPlayerStatus,
    DRAGONFLY_PLAYER_DEFAULT_WAIT_TIME,
)
import logging
from app.utils.ws_helpers import get_player_id_from_request, get_player_sid_from_request


logger = logging.getLogger(__name__)


def save_player_to_dragonfly_on_connect() -> None:
    player_id = get_player_id_from_request()
    player_sid = get_player_sid_from_request()

    if not player_id:
        message = (
            f"Impossible to extract player id on connection," f"player_id: {player_id}"
        )
        logger.error(message)
        WsPlayerService.emit_event_to_single_player(
            event=NoPlayerIdOrSidEventDTO(
                payload=NoPlayerIdOrSidPayloadDTO(
                    player_id=player_id, sid=player_sid, message=message
                )
            ),
            sid=player_sid,
        )
        return

    player = DragonflyPlayerDTO(
        id=player_id,
        sid=player_sid,
        status=DragonflyPlayerStatus.CONNECTED.value,
        wait_time=DRAGONFLY_PLAYER_DEFAULT_WAIT_TIME,
    )

    new_player = DragonflyPlayerRepository.save_player(player)
    if not new_player:
        message = f"Impossible to save the player: {player_id} in to drangolfy."
        logger.error(message)
        WsPlayerService.emit_event_to_single_player(
            event=PlayerNotSavedToDragonflyEventDTO(
                payload=PlayerNotSavedToDrangonflyPayloadDTO(
                    player_id=player_id, message=message
                )
            ),
            sid=player_sid,
        )
