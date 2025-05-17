from app import db
from uuid import UUID
from sqlalchemy import String
from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy.types import DATETIME
from datetime import datetime, timezone
from app.utils.constants import TableName

class Player(db.Model):
    __table_name__ = TableName.PLAYER

    id: Mapped[UUID] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(30))
    last_name: Mapped[str] = mapped_column(String(40))
    created_at: Mapped[datetime] = mapped_column(DATETIME(timezone=True), default= lambda: datetime.now(timezone.utc))
    updated_at: Mapped[datetime] = mapped_column(DATETIME(timezone=True), default= lambda: datetime.now(timezone.utc))
