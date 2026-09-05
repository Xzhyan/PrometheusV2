import getpass
from pathlib import Path

# Caminho absoluto
BASE_DIR = Path(__file__).resolve().parent.parent.parent

# Diretório de dados
DATA_DIR = BASE_DIR / 'data'

# Arquivo dos atalhos
JSON_FILE = DATA_DIR / 'shorts.json'

# Usuário
CURRENT_USER = getpass.getuser()


