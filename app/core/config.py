from pydantic_settings import BaseSettings, SettingsConfigDict
from pydantic import Field
from typing import Optional


class Settings(BaseSettings):
    # Variables de entorno
    ENVIRONMENT: str = Field("local", env="ENVIRONMENT")

    # URLs de la base de datos
    LOCAL_DATABASE_URL: str = Field("sqlite:///./local.db", env="LOCAL_DATABASE_URL")
    PROD_DATABASE_URL: str = Field(..., env="PROD_DATABASE_URL")  # Obligatoria en prod

    # Configuración de la base de datos a usar
    @property
    def DATABASE_URL(self) -> str:
        if self.ENVIRONMENT == "production":
            return self.PROD_DATABASE_URL
        return self.LOCAL_DATABASE_URL

    # ... (El resto de tu configuración de JWT, CORS, etc. se mantiene igual)

    model_config = SettingsConfigDict(
        env_file=".env",
        extra="ignore"
    )


settings = Settings()