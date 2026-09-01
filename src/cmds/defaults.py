from pathlib import Path

# core
from core.config import SHORT_JSON
from core.exceptions import MissingArgumentError

# utils
from utils.console import shutdown, restart, clear
from utils.functions import read_json, write_json


class Short:
    def __init__(self, entries: list[str]):
        if not len(entries) > 1:
            raise MissingArgumentError()

        self.shorts: dict = {} # atalhos

        self.loaded = False

        if not self.loaded:
            self.load(SHORT_JSON)

        cmd = entries[1]
        self.manage(cmd)


    def load(self, path: Path):
        """Carrega os dados do json de atalhos"""

        data = read_json(path)

        self.loaded = True

    def manage(self, cmd):
        """Controla o comando de atalhos"""

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
