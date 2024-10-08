from dotenv import load_dotenv
from pydantic import Field, ValidationError
from pydantic_settings import BaseSettings
from qna_api.crosscutting.logging import get_logger

load_dotenv()  

logger = get_logger(__name__)

class Settings(BaseSettings):
    database_url: str = Field(..., json_schema_extra={"env": "DATABASE_URL"})
    initial_admin_username: str = Field(..., json_schema_extra={"env": "INITIAL_ADMIN_USERNAME"})
    initial_admin_email: str = Field(..., json_schema_extra={"env": "INITIAL_ADMIN_EMAIL"})
    initial_admin_password: str = Field(..., json_schema_extra={"env": "INITIAL_ADMIN_PASSWORD"})
    secret_key: str = Field(..., json_schema_extra={"env": "SECRET_KEY"})
    algorithm: str = Field(..., json_schema_extra={"env": "ALGORITHM"})
    access_token_expire_minutes: int = Field(..., json_schema_extra={"env": "ACCESS_TOKEN_EXPIRE_MINUTES"})

    class Config:
        env_file = ".env"

try:
    settings = Settings()
except ValidationError as e:
    logger.error("Error loading settings: %s", e.json())
    raise

