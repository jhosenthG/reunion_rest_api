from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base
from app.core.config import settings

# Detectar si la URL es SQLite
is_sqlite = settings.DATABASE_URL.startswith("sqlite")

# Configurar el motor de SQLAlchemy
engine = create_engine(
    settings.DATABASE_URL,
    # Solo para SQLite: desactivar chequeo de hilo
    connect_args={"check_same_thread": False} if is_sqlite else {},
    # Habilitar pool y verificación de conexión
    pool_pre_ping=True,
    # Opcional: activa para ver SQL en desarrollo
    echo=False, # Cambiar a True si quieres ver las queries en consola
)

# Crear sesión local
SessionLocal = sessionmaker(
    autocommit=False,
    autoflush=False,
    bind=engine
)

# Base para modelos
Base = declarative_base()