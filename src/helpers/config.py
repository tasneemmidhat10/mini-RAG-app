try:
    from pydantic_settings import BaseSettings, SettingsConfigDict
except ImportError:
    from pydantic import BaseSettings
    SettingsConfigDict = None


class Settings(BaseSettings):
    APP_NAME: str
    APP_VERSION: str
    OPENAI_API_KEY: str

    FILE_ALLOWED_TYPE: list[str]
    FILE_MAX_SIZE: int
    FILE_DEFAULT_CHUNK_SIZE:int


    if SettingsConfigDict is not None:
        model_config = SettingsConfigDict(env_file=".env")
    else:
        class Config:
            env_file = ".env"


def get_settings():
    return Settings()
