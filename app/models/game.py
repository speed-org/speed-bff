from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import JSON, ForeignKey
from app import db
from app.utils.constants import TableName
from uuid import UUID
from datetime import datetime, timezone
from sqlalchemy.types import TIMESTAMP


class GameRoom(db.Model):  # type: ignore
    __table_name__ = TableName.GAME_STATE

    id: Mapped[UUID] = mapped_column(primary_key=True)
    isStarted: Mapped[bool] = mapped_column(default=False)
    isOver: Mapped[bool] = mapped_column(default=False)
    isMatched: Mapped[bool] = mapped_column(default=False)

    # Relationships
    hand1: Mapped[list[dict]] = mapped_column(JSON)
    hand2: Mapped[list[dict]] = mapped_column(JSON)
    leftMain: Mapped[list[dict]] = mapped_column(JSON)
    rightMain: Mapped[list[dict]] = mapped_column(JSON)
    leftHelper: Mapped[list[dict]] = mapped_column(JSON)
    rightHelper: Mapped[list[dict]] = mapped_column(JSON)

    player1Id: Mapped[UUID] = mapped_column(ForeignKey(f"{TableName.PLAYER}.id"))
    player2Id: Mapped[UUID] = mapped_column(ForeignKey(f"{TableName.PLAYER}.id"))

    created_at: Mapped[datetime] = mapped_column(
        TIMESTAMP(timezone=True), default=lambda: datetime.now(timezone.utc)
    )
    updated_at: Mapped[datetime] = mapped_column(
        TIMESTAMP(timezone=True), default=lambda: datetime.now(timezone.utc)
    )
