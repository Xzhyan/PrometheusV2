from pathlib import Path


# camingo absoluto
BASE_DIR = Path(__file__).resolve().parent.parent.parent

# Caminho do laucher .bat
BAT_LAUNCHER = BASE_DIR / 'prometheus.bat'

# Pasta de dados
DATA_DIR = BASE_DIR / 'data'

# Arquivo de atalhos do sistema
SHORTS_JSON = DATA_DIR / 'shorts.json'

