from datetime import datetime
from typing import Optional
from pydantic import BaseModel


class AppBase(BaseModel):
    name: str
    description: str
    db_name: str
    environment: str
    wallet_id: int


class AppCreate(AppBase):
    pass


class AppUpdate(BaseModel):
    name: Optional[str] = None
    description: Optional[str] = None
    db_name: Optional[str] = None
    environment: Optional[str] = None
    wallet_id: Optional[int] = None


class AppResponse(AppBase):
    id: int
    created_at: datetime
    updated_at: datetime
    
    class Config:
        from_attributes = True