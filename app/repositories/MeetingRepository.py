from datetime import datetime
from typing import List, Optional
from sqlalchemy.orm import Session
from sqlalchemy import and_

from app.models.meeting import Meeting
from app.models.user import User
from app.schemas.meeting import MeetingCreate, MeetingUpdate
from app.repositories.base import BaseRepository

class MeetingRepository(BaseRepository[Meeting, MeetingCreate, MeetingUpdate]):
    def __init__(self, db: Session):
        super().__init__(Meeting, db)

    def get_meetings_by_room_and_time(
        self, room_id: int, start_time: datetime, end_time: datetime
    ) -> List[Meeting]:
        """
        Obtiene reuniones que se solapan con el horario dado en una sala específica.
        """
        query = self.db.query(self.model).filter(
            and_(
                self.model.room_id == room_id,
                self.model.start_time < end_time,
                self.model.end_time > start_time,
            )
        )
        return query.all()

    def get_meetings_by_participant(self, user_id: int) -> List[Meeting]:
        """
        Obtiene todas las reuniones en las que participa un usuario.
        """
        query = self.db.query(self.model).join(self.model.participants).filter(User.id == user_id)
        return query.all()

    def create(self, obj_in: MeetingCreate, organizer: User) -> Meeting:
        """Crea una nueva reunión y la asocia con el organizador."""
        db_obj = self.model(
            title=obj_in.title,
            description=obj_in.description,
            start_time=obj_in.start_time,
            end_time=obj_in.end_time,
            room_id=obj_in.room_id,
            organizer=organizer,
        )
        self.db.add(db_obj)
        self.db.commit()
        self.db.refresh(db_obj)
        return db_obj