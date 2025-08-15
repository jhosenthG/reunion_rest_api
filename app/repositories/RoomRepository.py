from sqlalchemy.orm import Session
from sqlalchemy import and_

from app.models.room import Room
from app.schemas.room import RoomCreate, RoomUpdate
from app.repositories.base import BaseRepository


class RoomRepository(BaseRepository[Room, RoomCreate, RoomUpdate]):
    def __init__(self, db: Session):
        super().__init__(Room, db)

    def get_by_name(self, name: str) -> Room | None:
        """Obtiene una sala por su nombre."""
        return self.db.query(self.model).filter(self.model.name == name).first()

    def get_available_rooms(
            self,
            required_capacity: int,
            has_tv: bool = False,
            has_whiteboard: bool = False,
            has_projector: bool = False
    ) -> list[Room]:
        """
        Obtiene salas disponibles que cumplen con los criterios especificados.
        """
        query = self.db.query(self.model).filter(
            and_(
                self.model.capacity >= required_capacity,
                self.model.is_available == True
            )
        )

        if has_tv:
            query = query.filter(self.model.has_tv == True)
        if has_whiteboard:
            query = query.filter(self.model.has_whiteboard == True)
        if has_projector:
            query = query.filter(self.model.has_projector == True)

        return query.all()