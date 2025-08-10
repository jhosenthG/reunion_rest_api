# app/models/meeting.py
from sqlalchemy import Column, Integer, String, Boolean, DateTime, ForeignKey, Table
from sqlalchemy.orm import relationship
from app.core.database import Base

# Tabla intermedia para relación many-to-many entre Meeting y User (participantes)
meeting_participants = Table(
    "meeting_participants",
    Base.metadata,
    Column("meeting_id", Integer, ForeignKey("meetings.id"), primary_key=True),
    Column("user_id", Integer, ForeignKey("users.id"), primary_key=True),
)


class Meeting(Base):
    __tablename__ = "meetings"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String(100), nullable=False)
    description = Column(String(500))
    start_time = Column(DateTime, nullable=False)
    end_time = Column(DateTime, nullable=False)
    is_active = Column(Boolean, default=True)
    reminder_sent = Column(Boolean, default=False)  # Para recordatorios

    # Claves foráneas
    organizer_id = Column(Integer, ForeignKey("users.id"))
    room_id = Column(Integer, ForeignKey("rooms.id"))

    # Relaciones
    organizer = relationship("User", back_populates="organized_meetings", foreign_keys=[organizer_id])
    room = relationship("Room", back_populates="meetings")
    participants = relationship("User", secondary=meeting_participants, back_populates="participated_meetings")
