from app.repositories.dragonfly_matching_system import DragonflyMatchSystemRepository
from app.repositories.dragonfly_player import DragonflyPlayerRepository
from app.services.ws_room import WsRoomService
from app.utils.constants import NONE_STRING, DragonflyMatchingStatus
from app.dto.dragonfly_player import DragonflyPlayer
from app.repositories.dragonfly_room import DragonflyRoomRepository
import time
from app.dto.dragonfly_room import DragonflyRoomDTO
from uuid import uuid4
from app.utils.dragonfly_helpers import generate_room_key


def add_player_to_waitroom(player_id: str) -> tuple[dict, int]:
    """
    Add a player to the waiting room.
    """
    # TODO: solve for sid
    player = DragonflyPlayer(
        id=player_id,
        sid="",
        status=DragonflyMatchingStatus.WAITING.value,
        wait_time=int(time.time()),
    )
    current_info = DragonflyMatchSystemRepository.add_user_to_waitroom(player)

    if not current_info:
        return {"message": "Error trying to set new player to waiting room"}, 400

    return {
        "message": "Player added to waitroom",
        "current info": current_info,
    }, 200


def match_oldest_players() -> tuple[dict, int]:

    # First retrieving two oldest players ids
    player_ids = DragonflyMatchSystemRepository.get_two_oldest_players_ids()

    if len(player_ids) < 2:
        return {"message": "Not enough players to match"}, 200

    # Changing status
    players_status = (
        DragonflyMatchSystemRepository.change_matched_players_status_to_pending(
            player_ids[0], player_ids[1]
        )
    )

    room_dto = DragonflyRoomDTO(
        id=str(uuid4()),
        player1_id=player_ids[0],
        player2_id=player_ids[1],
        gamestate=None,
        is_active=False,
    )

    # Joining players into a room
    new_room_data = DragonflyRoomRepository.generate_room(room_dto)

    # Retrieving player socket_ids
    matched_players_socket_ids = [
        str(DragonflyPlayerRepository.get_socket_id(id)) for id in player_ids
    ]

    if len(matched_players_socket_ids) < 2 or any(
        id is NONE_STRING for id in matched_players_socket_ids
    ):
        return {"message": "Unexpected error trying to players socket ids."}, 400

    # Joining room
    WsRoomService.join_room(matched_players_socket_ids, generate_room_key(room_dto.id))

    return {
        "message": f"Sucessfully matched players:{player_ids} in room:{room_dto.id}.",
        "matched_ids": player_ids,
        "room_id": room_dto.id,
        "room_data": new_room_data,
        "new status": players_status,
    }, 200
