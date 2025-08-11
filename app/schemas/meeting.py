from datetime import datetime
from typing import List, Optional
from pydantic import BaseModel, field_validator

from app.schemas.user import UserBase  # Asumimos que ya existe
from app.schemas.room import RoomBase   # Asumimos que ya existe


class MeetingBase(BaseModel):
    title: str
    description: Optional[str] = None
    start_time: datetime
    end_time: datetime


class MeetingCreate(MeetingBase):
    organizer_id: int
    room_id: int
    participant_ids: List[int] = []  # IDs de usuarios que participarán

    @field_validator("end_time")
    def validate_time_range(cls, v, values):
        start_time = values.data.get("start_time")
        if start_time and v <= start_time:
            raise ValueError("La hora de finalización debe ser posterior a la de inicio.")
        return v


class MeetingUpdate(BaseModel):
    title: Optional[str] = None
    description: Optional[str] = None
    start_time: Optional[datetime] = None
    end_time: Optional[datetime] = None
    room_id: Optional[int] = None
    is_active: Optional[bool] = None
    participant_ids: Optional[List[int]] = None  # Permitir actualización de participantes

    @field_validator("end_time")
    def validate_time_range(cls, v, values):
        start_time = values.data.get("start_time")
        if start_time and v and v <= start_time:
            raise ValueError("La hora de finalización debe ser posterior a la de inicio.")
        return v


class MeetingRead(MeetingBase):
    id: int
    is_active: bool
    reminder_sent: bool
    created_at: datetime
    updated_at: Optional[datetime] = None

    # Relaciones (objetos completos, no solo IDs)
    organizer: UserBase
    room: RoomBase
    participants: List[UserBase]

    class Config:
        from_attributes = True