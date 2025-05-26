from app.dto.auth import RegisterPlayerDTO
from app.models.player import Player


class PostgresPlayerRepository:
    @staticmethod
    def add_player_to_database(player_dto: RegisterPlayerDTO) -> Player:
        """
        Adds player to PostgreSQL database.
        """
        added_player = Player(
            name = player_dto.name,
            last_name = player_dto.last_name,
            email = player_dto.email,
            firebase_id = player_dto.firebase_id,
            refresh_token = player_dto.refresh_token
        )
        
        added_player.save()

        return added_player

