import getpass
from pathlib import Path

# Caminho absoluto
BASE_DIR = Path(__file__).resolve().parent.parent.parent

# Diretório de dados
DATA_DIR = BASE_DIR / 'data'

# Usuário
CURRENT_USER = getpass.getuser()


