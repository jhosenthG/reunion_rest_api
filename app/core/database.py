from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

from app.core.config import settings

# Determina los argumentos de conexión basados en el motor de la base de datos
# y crea el motor de SQLAlchemy
if settings.DATABASE_URL.startswith("sqlite"):
    engine = create_engine(
        settings.DATABASE_URL,
        connect_args={"check_same_thread": False}  # Necesario para SQLite con FastAPI
    )
else:
    engine = create_engine(settings.DATABASE_URL)

# Crea la clase SessionLocal que se usará para obtener sesiones
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Base para las clases de modelos declarativos (tus tablas)
Base = declarative_base()

# --- Dependencia para FastAPI ---
# Esta función proporcionará la sesión a los endpoints
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()