from pydantic import BaseModel
from typing import Optional
from datetime import datetime


class RoomBase(BaseModel):
    name: str
    floor: str
    capacity: int


class RoomCreate(RoomBase):
    has_tv: bool = False
    has_whiteboard: bool = False
    has_projector: bool = False


class RoomUpdate(BaseModel):
    name: Optional[str] = None
    floor: Optional[str] = None
    capacity: Optional[int] = None
    has_tv: Optional[bool] = None
    has_whiteboard: Optional[bool] = None
    has_projector: Optional[bool] = None
    is_available: Optional[bool] = None


class RoomRead(RoomBase):
    id: int
    has_tv: bool
    has_whiteboard: bool
    has_projector: bool
    is_available: bool
    created_at: datetime
    updated_at: Optional[datetime] = None

    class Config:
        from_attributes = True