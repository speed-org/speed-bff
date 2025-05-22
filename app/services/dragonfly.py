from redis.commands.search.field import TagField, NumericField
from redis.commands.search.index_definition import IndexDefinition, IndexType
from redis import Redis


class DragonflyService:
    @staticmethod
    def init_player_index(r: Redis) -> None:
        try:
            r.ft("idx:players").info()  # Check if index exists
        except Exception:
            r.ft("idx:players").create_index(
                fields=[TagField("status"), NumericField("wait_time")],
                definition=IndexDefinition(
                    prefix=["player:"], index_type=IndexType.HASH
                ),
            )
