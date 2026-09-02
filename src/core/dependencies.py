# core
from .constants import DATA_DIR

def check_dependencies() -> bool:
    """Verifica as dependências da ferramenta"""

    # Cria a pasta 'data' se não existir
    DATA_DIR.mkdir(parents=True, exist_ok=True)

    return True


