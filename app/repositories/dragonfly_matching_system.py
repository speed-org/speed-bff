from app.utils.constants import DragonflyPlayerField, DragonflyPlayerStatus
from app import r
from app.dto.dragonfly_player import DragonflyPlayerDTO
from typing import Union
from app.utils.dragonfly_helpers import (
    create_player_key,
    get_player_id_from_key,
)
from redis.commands.search.query import Query


class DragonflyMatchSystemRepository:

    @staticmethod
    def add_user_to_waitroom(player: DragonflyPlayerDTO) -> Union[None, str]:
        """
        Adds user to Dragonfly database.
        """
        player_key = create_player_key(player.id)
        r.hset(player_key, DragonflyPlayerField.STATUS.value, player.status)
        r.hset(player_key, DragonflyPlayerField.WAIT_TIME.value, player.wait_time)

        new_status = r.hget(player_key, DragonflyPlayerField.STATUS.value)
        new_wait_time = r.hget(player_key, DragonflyPlayerField.WAIT_TIME.value)

        return f"status: {new_status}, wait_time: {new_wait_time}"

    @staticmethod
    def get_two_oldest_players_ids() -> list[str]:
        """
        Finds two oldest players in the waiting room.
        """
        # Search for all players w waiting status
        query_set = "{waiting}"
        waiting_players_query_str = f"@status:{query_set}"
        oldest_players = r.ft("idx:players").search(
            Query(waiting_players_query_str)
            .sort_by(DragonflyPlayerField.WAIT_TIME.value)
            .paging(0, 2)
        )

        oldest_player_ids = [
            get_player_id_from_key(doc.id)
            for doc in oldest_players.docs
            if doc.id is not None
        ]

        return oldest_player_ids

    @staticmethod
    def change_matched_players_status_to_pending(
        player1_id: str, player2_id: str
    ) -> tuple[str, str]:

        player1_key = create_player_key(player1_id)
        player2_key = create_player_key(player2_id)

        field = DragonflyPlayerField.STATUS.value
        value = DragonflyPlayerStatus.PENDING.value

        r.hset(player1_key, field, value)
        r.hset(player2_key, field, value)

        player1_new_status = r.hget(player1_key, field)
        player2_new_status = r.hget(player2_key, field)

        return player1_new_status, player2_new_status
