from app.dto.auth import (
    RegisterPlayerPayloadDTO,
    RegisterPlayerResponseDTO,
    LogInPlayerPayloadDTO,
    LogInPlayerResponseDTO,
)
from app.repositories.postgres_player import PostgresPlayerRepository
from app.utils.response_builder import ResponseBuilder
import logging
from flask import Response


logger = logging.getLogger(__name__)


def sign_up_player(player_dto: RegisterPlayerPayloadDTO) -> Response:
    """
    Adds player to PostgreSQL database.
    """
    logger.info(f"Trying to save player in postgres, id: {player_dto.firebaseId}")
    new_player = PostgresPlayerRepository.add_player_to_database(player_dto)

    if not new_player:
        message = (
            f"Error adding new player to database,"
            f" firebase id: {player_dto.firebaseId}."
        )
        logger.error(message)
        return ResponseBuilder.fail(message=message)

    logger.info(
        f"Player firebase_id: {player_dto.firebaseId}, successfully registered."
    )

    # Create ResponseDTO
    response_dto = RegisterPlayerResponseDTO(new_player.id)

    return ResponseBuilder.success(
        message="Player added to database", data=response_dto
    )


def log_in_player(player_dto: LogInPlayerPayloadDTO) -> Response:
    """
    Retrieves player information from PostreSQL database.
    """
    logger.info(
        f"Trying to retrieve player information from postgres, id:{player_dto.firebaseId}"
    )

    player_info = PostgresPlayerRepository.get_player_by_firebase_id(player_dto)

    if not player_info:
        message = (
            f"Error retrieving player information from database,"
            f" firebase id: {player_dto.firebaseId}"
        )
        logger.error(message)
        return ResponseBuilder.fail(message=message)

    logger.info(f"Player id: {player_info.id}, successfully retrieved.")

    # Create Response DTO
    response_dto = LogInPlayerResponseDTO(player_info.id)

    return ResponseBuilder.success(
        message="Player information retrieved", data=response_dto
    )
