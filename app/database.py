from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# Conexión para SQLite (archivo local)
SQLALCHEMY_DATABASE_URL = "sqlite:///./reunion.db"

engine = create_engine(
    SQLALCHEMY_DATABASE_URL,
    connect_args={"check_same_thread": False}  # Solo para SQLite
)
SessionLocal = sessionmaker(autocommit=False, bind=engine)
Base = declarative_base()