from app.dto.auth import RegisterPlayerDTO
from app.models.player import Player


class PostgresPlayerRepository:
    @staticmethod
    def add_player_to_database(player_dto: RegisterPlayerDTO) -> Player:
        """
        Adds player to PostgreSQL database.
        """
        added_player = Player(
            name=player_dto.name.lower(),
            last_name=player_dto.lastName.lower(),
            email=player_dto.email.lower(),
            firebase_id=player_dto.firebaseId,
            refresh_token=player_dto.refreshToken,
        )

        added_player.save()

        return added_player
