from pydantic import BaseSettings

class Settings(BaseSettings):
    """Application settings."""
    
    app_name: str = "Python API Demo"
    debug: bool = False
    api_prefix: str = "/api/v1"
    
    class Config:
        env_file = ".env"

settings = Settings()