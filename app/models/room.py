from sqlalchemy import Column, Integer, String, Boolean, DateTime
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func
from app.database import Base


class Room(Base):
    __tablename__ = "rooms"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(100), unique=True, nullable=False, index=True)
    floor = Column(String(50), nullable=False)
    capacity = Column(Integer, nullable=False)

    # Amenidades de la sala
    has_tv = Column(Boolean, default=False)
    has_whiteboard = Column(Boolean, default=False)
    has_projector = Column(Boolean, default=False)
    is_available = Column(Boolean, default=True)

    # Timestamps
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    updated_at = Column(DateTime(timezone=True), onupdate=func.now())

    # Relación con reuniones
    meetings = relationship("Meeting", back_populates="room")

    def __repr__(self):
        return f"<Room(id={self.id}, name='{self.name}', floor='{self.floor}')>"