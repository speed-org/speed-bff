
from app.dto.auth import RegisterPlayerDTO
from app.repositories.postgres_player import PostgresPlayerRepository
from app.utils.response_builder import ResponseBuilder
import logging

logger = logging.getLogger(__name__)


def sign_up_player(player_dto: RegisterPlayerDTO) -> tuple[dict, int]:
    """
    Adds player to PostgresSQL database.
    """    
    logger.info(f"Trying to save player in postgres, id: {player_dto.firebase_id}")
    new_player = PostgresPlayerRepository.add_player_to_database(player_dto)

    if not new_player:
        message = f"Error adding new player to database, firebase id: {player_dto.firebase_id}."
        logger.error(message)
        return ResponseBuilder.fail(message=message)
    
    logger.info(f"Player id: {player_dto.firebase_id}, successfully registered.")
    
    return ResponseBuilder.success(
        message="Player added to database",
        data={"current player info": new_player}
    )

