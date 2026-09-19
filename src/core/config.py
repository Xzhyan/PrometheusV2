from pydantic_settings import BaseSettings, SettingsConfigDict

class Settings(BaseSettings):
    """Configurações"""

    TOOL_NAME: str = "Prometheus"
    VERSION: str = "2.0"

    AUTHOR: str = "Nxtvsdev"
    TEAM: str = "Bravo Dynamics"

    # # mais tarde configuro o .env
    # model_config = SettingsConfigDict(
    #     env_file=".env"
    # )

settings = Settings()
