from app.utils.constants import (
    DragonflyWaitroomField,
    DragonflyPlayerField,
    DragonflyPlayerStatus,
)
from app import r
from typing import Optional
from app.utils.dragonfly_helpers import (
    get_id_from_key,
    generate_waitroom_key,
)
from redis.commands.search.query import Query
from app.repositories.dragonfly_player import DragonflyPlayerRepository
from app.dto.dragonfly_waitroom import DragonflyWaitroomDTO
from typing import Any

# Using this class to directly interact with Dragonfly about Matching System


class DragonflyWaitroomRepository:

    @staticmethod
    def generate_waitingroom(
        waitroom_dto: DragonflyWaitroomDTO,
    ) -> Optional[dict[str, str]]:
        """
        Generates waitingroom key and uploads room info to database.
        """
        waitroom_key = generate_waitroom_key(waitroom_dto.id)
        r.hset(
            waitroom_key,
            mapping={
                DragonflyWaitroomField.PLAYER1_ID.value: waitroom_dto.player1_id,
                DragonflyWaitroomField.PLAYER2_ID.value: waitroom_dto.player2_id,
                DragonflyWaitroomField.PLAYER1_ACCEPTED.value: waitroom_dto.player1_accepted,
                DragonflyWaitroomField.PLAYER1_ACCEPTED.value: waitroom_dto.player2_accepted,
            },
        )

        new_waitroom: dict[str, Any] = r.hgetall(waitroom_key)

        return new_waitroom

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
            get_id_from_key(doc.id) for doc in oldest_players.docs if doc.id is not None
        ]

        return oldest_player_ids

    @staticmethod
    def change_matched_players_status_to_pending(
        player1_id: str, player2_id: str
    ) -> tuple[Optional[str], Optional[str]]:

        new_status = DragonflyPlayerStatus.PENDING.value

        player1_new_status = DragonflyPlayerRepository.update_player_status(
            player1_id, new_status
        )
        player2_new_status = DragonflyPlayerRepository.update_player_status(
            player2_id, new_status
        )

        return player1_new_status, player2_new_status
