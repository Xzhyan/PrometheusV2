from pydantic_settings import BaseSettings, SettingsConfigDict
from pathlib import Path
from colorama import Fore as fg

# Caminho absoluto
BASE_DIR = Path(__file__).resolve().parent.parent.parent

# Caminho do .env file
ENV_FILE = BASE_DIR / '.env'

# Caminho do diretório de dados
DATA_DIR = BASE_DIR / 'data'

# Caminho dos logs
LOG_DIR = BASE_DIR / 'logs'

# Arquivo de atalhos
SHORT_JSON = DATA_DIR / 'shorts.json'


class Colors:
    """Definição de cores da ferramenta"""

    # Textos
    TEXT_ONE = fg.RED
    TEXT_TWO = fg.LIGHTWHITE_EX

    # Tool
    FG_ONE = fg.RED
    FG_TWO = fg.LIGHTWHITE_EX

    # Alertas
    INFO = fg.BLUE
    SUCCESS = fg.GREEN
    ERROR = fg.RED
    WARNING = fg.YELLOW


class Settings(BaseSettings):
    """Configurações da ferramenta"""

    # Informações da tool
    TOOL_NAME: str
    VERSION: str

    # Informações do dev.
    AUTHOR: str
    TEAM: str


    model_config = SettingsConfigDict(
        env_file=ENV_FILE
    )

settings = Settings()
