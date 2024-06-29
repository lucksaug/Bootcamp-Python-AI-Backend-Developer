from pydantic_settings import BaseSettings, SettingsConfigDict
from dotenv import load_dotenv
import os
from pathlib import Path

ROOT_FILE_PATH = Path(__file__).parent


class Settings(BaseSettings):
    load_dotenv()
    PROJECT_NAME: str = "Store API"
    ROOT_PATH: str = "/"
    DATABASE_URL: str = os.getenv("DATABASE_URL")
    model_config = SettingsConfigDict(env_file=ROOT_FILE_PATH / ".env")


settings = Settings()
