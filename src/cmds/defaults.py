from pathlib import Path

# core
from core.config import SHORT_JSON
from core.exceptions import MissingArgumentError

# utils
from utils.console import shutdown, restart, clear


class Short:
    def __init__(self, entries: list[str]):
        pass


DEFAULT_COMMANDS = {
    'exit': {
        'desc': "finaliza a ferramenta",
        'handler': shutdown
    },
    'restart': {
        'desc': "reinicia a ferramenta",
        'handler': restart
    },
    'clear': {
        'desc': "limpa a tela da ferramenta",
        'handler': clear
    },
    'short': {
        'desc': "atalhos personalizados",
        'handler': lambda entries: Short(entries)
    }
}
