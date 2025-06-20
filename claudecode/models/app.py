from datetime import datetime
from sqlalchemy import String, Integer, DateTime, func
from sqlalchemy.orm import Mapped, mapped_column
from .base import Base


class App(Base):
    __tablename__ = "apps"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    name: Mapped[str] = mapped_column(String, nullable=False)
    description: Mapped[str] = mapped_column(String, nullable=False)
    db_name: Mapped[str] = mapped_column(String, nullable=False)
    enviroment: Mapped[str] = mapped_column(String, nullable=False)
    wallet_id: Mapped[int] = mapped_column(Integer, nullable=False)
    created_at: Mapped[datetime] = mapped_column(DateTime, default=func.now, nullable=False)
    updated_at: Mapped[datetime] = mapped_column(
        DateTime, default=func.now, onupdate=func.now, nullable=False)
