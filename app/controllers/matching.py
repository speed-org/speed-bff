from dataclasses import asdict
from app.repositories.dragonfly_waitroom import DragonflyWaitroomRepository
from app.repositories.dragonfly_player import DragonflyPlayerRepository
from app.dto.dragonfly_waitroom import DragonflyWaitroomDTO
from app.utils.constants import DragonflyPlayerStatus
from app.utils.dragonfly_helpers import generate_random_id


def add_player_to_matching_system(player_id: str) -> tuple[dict, int]:
    """
    Changes player's status to waiting and adds a wait_time.
    """

    desired_status = DragonflyPlayerStatus.WAITING.value

    new_status = DragonflyPlayerRepository.update_player_status(
        player_id, desired_status
    )
    new_wait_time = DragonflyPlayerRepository.update_player_wait_time(player_id)

    current_info = f"status: {new_status}, wait_time: {new_wait_time}"

    if not current_info:
        return {"message": "Error trying to set new player to waiting room"}, 400

    return {
        "message": "Player added to waitroom",
        "current player info": current_info,
    }, 200


def match_oldest_players() -> tuple[dict, int]:

    # Retrieve two oldest player ids
    player_ids = DragonflyWaitroomRepository.get_two_oldest_players_ids()

    if len(player_ids) < 2:
        return {"message": "Not enough players to match"}, 200

    # Players matched! --> WaitroomDTO
    waitroom_dto = DragonflyWaitroomDTO(
        id=generate_random_id(),
        player1_id=player_ids[0],
        player2_id=player_ids[1],
        player1_accepted=False,
        player2_accepted=False,
    )

    # Adding waitroom to dragonfly database
    waitroom_data = DragonflyWaitroomRepository.generate_waitingroom(waitroom_dto)

    if not waitroom_data:
        return {"message": "Impossible to save waiting room to the database."}, 400

    # Updating players status to 'pending'
    players_status = (
        DragonflyWaitroomRepository.change_matched_players_status_to_pending(
            player_ids[0], player_ids[1]
        )
    )

    return {
        "message": "Sucessfully matched players.",
        "matched_ids": player_ids,
        "waitroom_data": asdict(waitroom_dto),
        "new status": players_status,
    }, 200

    # -------------------------------------------------------

    # # Creating RoomDTO
    # room_dto = DragonflyRoomDTO(
    #     id=generate_random_id(),
    #     player1_id=player_ids[0],
    #     player2_id=player_ids[1],
    #     gamestate=None,
    # )

    # # Generating roomkey and uploading to database
    # new_room_data = DragonflyRoomRepository.generate_room(room_dto)

    # # Retrieving player socket_ids
    # matched_players_socket_ids = [
    #     str(DragonflyPlayerRepository.get_socket_id(id)) for id in player_ids
    # ]

    # if len(matched_players_socket_ids) < 2 or any(
    #     id is NONE_STRING for id in matched_players_socket_ids
    # ):
    #     return {"message": "Unexpected error trying to players socket ids."}, 400

    # # Joining players to room
    # WsRoomService.join_room(matched_players_socket_ids,
    # generate_room_key(room_dto.id))
