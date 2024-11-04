from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    model_config = SettingsConfigDict(
        env_file=".env",
        env_file_encoding="utf-8",
        case_sensitive=True,
    )

    ENV: str = "local"
    DEBUG: bool = True
    TITLE: str = "FastAPI App"
    VERSION: str = "0.0.1"
    APP_HOST: str = "127.0.0.1"
    APP_PORT: int = 8000
    CORS_ORIGINS: list[str] = [
        "http://localhost:8000",
        "http://127.0.0.1:8000",
    ]


def get_settings() -> Settings:
    return Settings()


settings: Settings = get_settings()
