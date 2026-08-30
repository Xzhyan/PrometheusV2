
# core
from core.config import DATA_DIR, LOG_DIR


# utils
from utils.functions import check_file, check_folder


def check_dependencies():
    """Verifica as dependências da ferramenta"""

    folders = [
        DATA_DIR,
        LOG_DIR
    ]

    for folder in folders:
        check_folder(folder, create=True)

    return True


