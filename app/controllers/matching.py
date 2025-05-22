from app.repositories.dragonfly_matching_system import DragonflyMatchSystemRepository
from app.utils.constants import DragonflyMatchingStatus
from app.dto.dragonfly_player import DragonflyPlayer
import time


def add_player_to_waitroom(player_id: str) -> tuple[dict, int]:
    """
    Add a player to the waiting room.
    """
    player = DragonflyPlayer(
        player_id, DragonflyMatchingStatus.WAITING.value, int(time.time())
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

    return {
        "message": f"Sucessfully matched {player_ids}",
        "new status": players_status,
    }, 200
