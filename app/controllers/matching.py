from app.repositories.dragonfly_matching_system import DragonflyMatchSystemRepository
from app.utils.constants import DragonflyMatchingStatus
from app.dto.dragonfly_player import DragonflyPlayer

def add_player_to_waitroom(player_id):
    """
    Add a player to the waiting room.
    """
    player = DragonflyPlayer(player_id, DragonflyMatchingStatus.WAITING.value)
    current_status = DragonflyMatchSystemRepository.add_user_to_waitroom(player)

    if not current_status:
        return {"message": "Error trying to set new player to waiting room"}, 400
        
    return {"message": "Player added to waitroom", "current status": current_status}, 200
