# app/config.py

from pydantic_settings import BaseSettings  # updated import
from typing import List, Optional

class Settings(BaseSettings):
    DOWNLOAD_DIR: str = "downloads"
    ALLOWED_ORIGINS: List[str] = ["*"]
    AWS_S3_BUCKET: Optional[str] = None
    AWS_ACCESS_KEY: Optional[str] = None
    AWS_SECRET_KEY: Optional[str] = None

settings = Settings()
