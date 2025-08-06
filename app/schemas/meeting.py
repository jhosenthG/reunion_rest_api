from pydantic import BaseModel
from typing import Optional
from datetime import datetime


class MeetingBase(BaseModel):
    title: str
    description: Optional[str] = None
    start_time: datetime
    end_time: datetime
    organizer_id: int
    room_id: int


class MeetingCreate(MeetingBase):
    pass  # Puedes extenderlo más adelante si necesitas campos adicionales en creación


class MeetingUpdate(BaseModel):
    title: Optional[str] = None
    description: Optional[str] = None
    start_time: Optional[datetime] = None
    end_time: Optional[datetime] = None
    is_active: Optional[bool] = None
    room_id: Optional[int] = None


class MeetingRead(MeetingBase):
    id: int
    is_active: bool
    reminder_sent: bool
    created_at: datetime
    updated_at: Optional[datetime] = None

    class Config:
        from_attributes = True