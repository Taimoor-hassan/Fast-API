import os
from functools import lru_cache
from pydantic_settings import BaseSettings
from pathlib import Path
from dotenv import load_dotenv
from urllib.parse import quote_plus

env_path = Path(".") / ".env"
load_dotenv(dotenv_path=env_path)


class Settings(BaseSettings):

    # App
    APP_NAME:  str = os.environ.get("APP_NAME", "FastAPI")
    DEBUG: bool = bool(os.environ.get("DEBUG", False))

    # Postgresql Database Config
    SQL_HOST: str = os.environ.get("SQL_HOST", 'localhost')
    SQL_USER: str = os.environ.get("SQL_USER", 'root')
    SQL_PASS: str = os.environ.get("SQL_PASSWORD", 'secret')
    SQL_PORT: int = int(os.environ.get("SQL_PORT", 5432))
    SQL_DB: str = os.environ.get("SQL_DB", 'fastapi')
    DATABASE_URI: str = f"postgresql://{SQL_USER}:%s@{SQL_HOST}:{SQL_PORT}/{SQL_DB}" % quote_plus(SQL_PASS)

    # App Secret Key
    SECRET_KEY: str = os.environ.get("SECRET_KEY", "8deadce9449770680910741063cd0a3fe0acb62a8978661f421bbcbb66dc41f1")


@lru_cache()
def get_settings() -> Settings:
    return Settings()
