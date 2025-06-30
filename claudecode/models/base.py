from sqlalchemy.ext.asyncio import AsyncAttrs
from sqlalchemy.orm import DeclarativeBase


class Base(AsyncAttrs, DeclarativeBase):
    """Base class for all SQLAlchemy models.
    
    Provides async capabilities and serves as the declarative base
    for all database models in the application.
    """
    pass