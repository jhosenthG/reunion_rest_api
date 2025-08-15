from sqlalchemy.orm import Session
from app.models.user import User
from app.schemas.user import UserCreate, UserUpdate
from app.repositories.base import BaseRepository

class UserRepository(BaseRepository[User, UserCreate, UserUpdate]):
    def __init__(self, db: Session):
        super().__init__(User, db)

    def get_by_email(self, email: str) -> User | None:
        return self.db.query(self.model).filter(self.model.email == email).first()

    def get_active_users(self) -> list[User]:
        # ✅ Esta es la forma correcta de filtrar: usando un operador de comparación
        return self.db.query(self.model).filter(self.model.is_active == True).all()