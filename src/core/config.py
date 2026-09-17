from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    """Configurações básicas"""

    # Ferramenta
    TOOL_NAME: str = "Prometheus"
    VERSION: str = "2.0"

    # Autor
    AUTHOR: str = "Nxtvsdev"
    TEAM: str = "Bravo Dynamics"

    # vou configurar por ultimo
    # model_config = SettingsConfigDict(
    #     env_file=
    # )

settings = Settings()
