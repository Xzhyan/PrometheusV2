from pathlib import Path

# core
from core.constants import DATA_DIR, SHORTS_JSON

# utils
from utils.functions import write_json


def check() -> bool:
    """Verifica as dependencias da ferramenta"""

    DIR_LIST: list[Path] = [
        DATA_DIR
    ]

    # Garante que pasta necessarias sejam criadas se não existirem
    for dir in DIR_LIST:
        print(f"Verificando: {dir}")

        dir.mkdir(exist_ok=True)

    # Verifica se o arquivo de shorts.json existe
    if not SHORTS_JSON.is_file():
        data = {
            'app': {},
            'dir': {}
        }

        write_json(SHORTS_JSON, data)

    return True
