from pydantic_settings import BaseSettings, SettingsConfigDict
from typing import Optional
from dotenv import load_dotenv
load_dotenv()

class Settings(BaseSettings):
    # LLM_PROVIDER: str = "gemini"  # Default to gemini now
    OPENAI_API_KEY: Optional[str] = None
    ANTHROPIC_API_KEY: Optional[str] = None
    GEMINI_API_KEY: Optional[str] = None
    XAI_API_KEY: Optional[str] = None
    
    # MongoDB Config
    MONGO_URI: str = "mongodb://localhost:27017" # Replace with your URI in .env
    MONGO_DB: str = "chatbot_db" # Replace with your DB name
    SERVICE_COLLECTION: str = "service"
    PROFEAAIONAL_COLLECTION: str = "professionals"
    USERS_COLLECTION: str = "users"

    model_config = SettingsConfigDict(
        env_file=".env", 
        env_file_encoding="utf-8", 
        extra="ignore"
    )

settings = Settings()
