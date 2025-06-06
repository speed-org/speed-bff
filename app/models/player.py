from app import db
from sqlalchemy import String
from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy.types import TIMESTAMP
from datetime import datetime, timezone
from app.utils.constants import TableName
import uuid


class Player(db.Model):  # type: ignore
    __table_name__ = TableName.PLAYER

    id: Mapped[str] = mapped_column(
        String(36), primary_key=True, default=lambda: str(uuid.uuid4())
    )
    name: Mapped[str] = mapped_column(String(30))
    last_name: Mapped[str] = mapped_column(String(40))
    email: Mapped[str] = mapped_column(String(80))
    firebase_id: Mapped[str] = mapped_column(String(100))
    refresh_token: Mapped[str] = mapped_column(String(512))
    created_at: Mapped[datetime] = mapped_column(
        TIMESTAMP(timezone=True), default=lambda: datetime.now(timezone.utc)
    )
    updated_at: Mapped[datetime] = mapped_column(
        TIMESTAMP(timezone=True), default=lambda: datetime.now(timezone.utc)
    )

    def __repr__(self) -> str:
        return (
            f"<Player: id: {self.id},"
            f" email: {self.email},"
            f" firebase_id: {self.firebase_id}"
        )

    def save(self) -> None:
        db.session.add(self)
        db.session.commit()
