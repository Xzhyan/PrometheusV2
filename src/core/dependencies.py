import time
from pathlib import Path

# core
from core.constants import DATA_DIR, SHORTS_JSON, URL_JSON, URL_DICT

# utils
from utils.functions import write_json

# ui
from ui.ui_console import alert


def check() -> bool:
    """Verifica as dependencias da ferramenta"""

    DIR_LIST: list[Path] = [
        DATA_DIR
    ]

    # Garante que pasta necessarias sejam criadas se não existirem
    for dir in DIR_LIST:
        alert('info', f"Verificando caminho: {dir}...", False)
        time.sleep(0.5)

        dir.mkdir(exist_ok=True)

        alert('success', f"{dir}: verificado com sucesso!")
        time.sleep(0.5)

    # Verifica se o arquivo de shorts.json existe
    if not SHORTS_JSON.is_file():
        data = {
            'app': {},
            'dir': {}
        }

        write_json(SHORTS_JSON, data)

    # Verifica se o arquivo urls.json existe
    if not URL_JSON.is_file():
        data = URL_DICT
        write_json(URL_JSON, data)

    return True
