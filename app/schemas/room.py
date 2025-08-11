from datetime import datetime
from typing import Optional
from pydantic import BaseModel, field_validator


class RoomBase(BaseModel):
    name: str
    floor: str
    capacity: int


class RoomCreate(RoomBase):
    has_tv: bool = False
    has_whiteboard: bool = False
    has_projector: bool = False

    @field_validator("capacity")
    def validate_capacity(cls, v):
        if v < 1:
            raise ValueError("La capacidad debe ser mayor o igual a 1.")
        return v

    @field_validator("name")
    def validate_name(cls, v):
        if not v.strip():
            raise ValueError("El nombre no puede estar vacío o ser solo espacios.")
        return v.strip()


class RoomUpdate(BaseModel):
    name: Optional[str] = None
    floor: Optional[str] = None
    capacity: Optional[int] = None
    has_tv: Optional[bool] = None
    has_whiteboard: Optional[bool] = None
    has_projector: Optional[bool] = None
    is_available: Optional[bool] = None

    @field_validator("capacity")
    def validate_capacity(cls, v):
        if v is not None and v < 1:
            raise ValueError("La capacidad debe ser mayor o igual a 1.")
        return v


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