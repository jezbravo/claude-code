from datetime import datetime
from typing import Optional
from pydantic import BaseModel


class AppBase(BaseModel):
    """Base Pydantic model for application data.
    
    Contains common fields shared across different application schemas.
    
    Attributes:
        name: Application name
        description: Application description
        db_name: Database name for the application
        environment: Deployment environment
        wallet_id: Associated wallet identifier
        status: Application status, defaults to 'active'
    """
    name: str
    description: str
    db_name: str
    environment: str
    wallet_id: int
    status: str = "active"


class AppCreate(AppBase):
    """Pydantic model for creating new applications.
    
    Inherits all fields from AppBase without modifications.
    Used for API request validation when creating applications.
    """
    pass


class AppUpdate(BaseModel):
    """Pydantic model for updating existing applications.
    
    All fields are optional, allowing partial updates of application data.
    
    Attributes:
        name: Optional new application name
        description: Optional new application description
        db_name: Optional new database name
        environment: Optional new environment
        wallet_id: Optional new wallet identifier
        status: Optional new status
    """
    name: Optional[str] = None
    description: Optional[str] = None
    db_name: Optional[str] = None
    environment: Optional[str] = None
    wallet_id: Optional[int] = None
    status: Optional[str] = None


class AppResponse(AppBase):
    """Pydantic model for application API responses.
    
    Extends AppBase with additional fields that are populated
    when retrieving application data from the database.
    
    Attributes:
        id: Application primary key
        created_at: Application creation timestamp
        updated_at: Last update timestamp
    """
    id: int
    created_at: datetime
    updated_at: datetime
    
    class Config:
        """Pydantic configuration for AppResponse model.
        
        Enables ORM mode to work with SQLAlchemy models.
        """
        from_attributes = True