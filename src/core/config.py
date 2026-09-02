from pydantic_settings import BaseSettings



class Settings(BaseSettings):
    """Configurações da ferramenta"""

    # Ferramenta
    TOOL_NAME: str = "Prometheus"
    VERSION: str = "2.0"

    # Author
    AUTHOR: str = "Nxtvsdev"
    TEAM: str = "Bravo Dynamics"


settings = Settings()
