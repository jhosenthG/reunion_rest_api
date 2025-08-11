from sqlalchemy import Column, Integer, String, Boolean, DateTime, ForeignKey, Table
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func
from app.core.database import Base

# Tabla intermedia para la relación many-to-many entre Meeting y User (participantes)
meeting_participants = Table(
    "meeting_participants",
    Base.metadata,
    Column("meeting_id", Integer, ForeignKey("meetings.id"), primary_key=True),
    Column("user_id", Integer, ForeignKey("users.id"), primary_key=True),
    # Índice para búsquedas eficientes por usuario o reunión
    extend_existing=True,
)


class Meeting(Base):
    __tablename__ = "meetings"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String(100), nullable=False, index=True)
    description = Column(String(500), nullable=True)
    start_time = Column(DateTime(timezone=True), nullable=False)
    end_time = Column(DateTime(timezone=True), nullable=False)
    is_active = Column(Boolean, default=True)
    reminder_sent = Column(Boolean, default=False)  # Para controlar recordatorios

    # Claves foráneas
    organizer_id = Column(Integer, ForeignKey("users.id"), nullable=False)
    room_id = Column(Integer, ForeignKey("rooms.id"), nullable=False)

    # Relaciones
    organizer = relationship(
        "User",
        back_populates="organized_meetings",
        foreign_keys=[organizer_id]
    )
    room = relationship("Room", back_populates="meetings")
    participants = relationship(
        "User",
        secondary=meeting_participants,
        back_populates="participated_meetings"
    )

    # Timestamps
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    updated_at = Column(DateTime(timezone=True), onupdate=func.now())

    def __repr__(self):
        return f"<Meeting(id={self.id}, title='{self.title}', start_time='{self.start_time}', room_id={self.room_id})>"

    def __str__(self):
        return f"{self.title} ({self.start_time} - {self.end_time})"