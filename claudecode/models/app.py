from datetime import datetime
from sqlalchemy import String, Integer, DateTime, func
from sqlalchemy.orm import Mapped, mapped_column
from .base import Base


class App(Base):
    """SQLAlchemy model representing an application.
    
    Stores application metadata including name, description, database configuration,
    environment details, and associated wallet information.
    
    Attributes:
        id: Primary key for the application
        name: Application name
        description: Application description
        db_name: Database name for the application
        environment: Deployment environment (dev, staging, prod)
        wallet_id: Associated wallet identifier
        status: Application status (active, inactive)
        created_at: Timestamp when the application was created
        updated_at: Timestamp when the application was last updated
    """
    __tablename__ = "apps"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    name: Mapped[str] = mapped_column(String, nullable=False)
    description: Mapped[str] = mapped_column(String, nullable=False)
    db_name: Mapped[str] = mapped_column(String, nullable=False)
    environment: Mapped[str] = mapped_column(String, nullable=False)
    wallet_id: Mapped[int] = mapped_column(Integer, nullable=False)
    status: Mapped[str] = mapped_column(String, nullable=False, default="active")
    created_at: Mapped[datetime] = mapped_column(DateTime, default=func.now(), nullable=False)
    updated_at: Mapped[datetime] = mapped_column(
        DateTime, default=func.now(), onupdate=func.now(), nullable=False)
