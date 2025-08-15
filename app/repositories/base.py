from typing import TypeVar, Generic, Type, Any
from sqlalchemy.orm import Session
from sqlalchemy import select

# Define un tipo genérico para el modelo de SQLAlchemy
ModelType = TypeVar("ModelType")
CreateSchemaType = TypeVar("CreateSchemaType")
UpdateSchemaType = TypeVar("UpdateSchemaType")


class BaseRepository(Generic[ModelType, CreateSchemaType, UpdateSchemaType]):
    """
    Clase base genérica para las operaciones CRUD.
    """

    def __init__(self, model: Type[ModelType], db: Session):
        self.model = model
        self.db = db

    def create(self, obj_in: CreateSchemaType) -> ModelType:
        """Crea un nuevo registro en la base de datos."""
        obj_data = obj_in.model_dump()
        db_obj = self.model(**obj_data)
        self.db.add(db_obj)
        self.db.commit()
        self.db.refresh(db_obj)
        return db_obj

    def get(self, id: Any) -> ModelType | None:
        """Obtiene un registro por su ID."""
        return self.db.get(self.model, id)

    def get_all(self, skip: int = 0, limit: int = 100) -> list[ModelType]:
        """Obtiene todos los registros con paginación."""
        stmt = select(self.model).offset(skip).limit(limit)
        return list(self.db.scalars(stmt))

    def update(self, db_obj: ModelType, obj_in: UpdateSchemaType) -> ModelType:
        """Actualiza un registro existente."""
        for field, value in obj_in.model_dump(exclude_unset=True).items():
            setattr(db_obj, field, value)
        self.db.add(db_obj)
        self.db.commit()
        self.db.refresh(db_obj)
        return db_obj

    def delete(self, db_obj: ModelType) -> ModelType:
        """Elimina un registro."""
        self.db.delete(db_obj)
        self.db.commit()
        return db_obj