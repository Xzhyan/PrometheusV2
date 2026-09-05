from pathlib import Path

# core
from .constants import DATA_DIR, JSON_FILE

# utils
from utils.functions import write_json


def check_dependencies() -> bool:
    """Verifica as dependências da ferramenta"""

    # Cria a pasta 'data' se não existir
    DATA_DIR.mkdir(parents=True, exist_ok=True)

    # Verifica se o shorts.json existe
    # se não existir já cria no formato correto
    if not JSON_FILE.exists():
        data: dict = {
            'app': {},
            'dir': {}
        }
        write_json(JSON_FILE, data)

    return True


