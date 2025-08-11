from sqlalchemy import Column, Integer, String, Boolean, DateTime
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func
from app.core.database import Base
from app.models.meeting import meeting_participants


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    username = Column(String(50), unique=True, nullable=False, index=True)
    email = Column(String(100), unique=True, nullable=False, index=True)
    password = Column(String(255), nullable=False)  # Hash de la contraseña
    is_active = Column(Boolean, default=True)
    is_admin = Column(Boolean, default=False)

    # Timestamps
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    updated_at = Column(DateTime(timezone=True), onupdate=func.now())

    # Relaciones
    # Un usuario puede organizar muchas reuniones
    organized_meetings = relationship("Meeting", back_populates="organizer", foreign_keys="Meeting.organizer_id")

    # Un usuario puede participar en muchas reuniones (many-to-many)
    participated_meetings = relationship("Meeting", secondary=meeting_participants, back_populates="participants")

    def __repr__(self):
        return f"<User(id={self.id},username='{self.username}',email='{self.email}')>"
