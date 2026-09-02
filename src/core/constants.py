import getpass
from pathlib import Path

# Caminho absoluto
BASE_DIR = Path(__file__).resolve().parent.parent.parent

# Usuário
CURRENT_USER = getpass.getuser()


