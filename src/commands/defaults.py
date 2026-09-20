

# utils
from utils.system import shutdown, clear, restart, list_commands
from utils.functions import read_json, write_json

# core
from core.constants import SHORTS_JSON


def show_default_cmds():
    """Exibe os comandos normais"""

    list_commands("Comandos Normais", DEFAULT_CMDS)


CATEGORIES: dict = {
    'defaults': {
        'desc': "Exibe a lista de comandos normais",
        'usage': "defaults",
        'handler': show_default_cmds
    },
}


def help_menu(*args):
    """Exibe o menu de ajuda e comandos da ferramenta"""

    list_commands("Categorias de Comandos", CATEGORIES)


class Short:
    shorts = read_json(SHORTS_JSON)

    def __init__(self):
        self.SHORT_CMDS: dict = {
            'add': {
                'desc': "adiciona um atalho",
                'handler': self.add
            },
            'list': {
                'desc': "lista todos os atalhos",
                'handler': self.list
            },
            'remove': {
                'desc': "remove um atalho",
                'handler': self.remove
            },
        }

    def add(self):
        print(self.shorts)

    def list(self):
        for short, data in self.shorts.items():
            print(f"short")
            for name in data:
                print(name)

    def remove(self):
        pass

    def dispatch(self, args):
        if len(args) <= 1:
            raise ValueError("esse comando utiliza mais argumentos: add/list/remove")

        arg = args[1]

        if arg in self.SHORT_CMDS:
            self.SHORT_CMDS[arg]['handler']()

        else:
            raise ValueError("erro no argumento passado")



DEFAULT_CMDS: dict = {
    'exit': {
        'desc': "Finaliza a ferramenta",
        'usage': "exit",
        'handler': shutdown
    },
    'clear': {
        'desc': "Limpa a tela da ferramenta",
        'usage': "clear",
        'handler': clear
    },
    'help': {
        'desc': "Exibe o menu de ajuda",
        'usage': "help",
        'handler': help_menu
    },
    'restart': {
        'desc': "Reinicia a ferramenta",
        'usage': "restart",
        'handler': restart
    },
    'short': {
        'desc': "Atalhos personalizadios",
        'usage': "add/list/remove ex: short add",
        'handler': lambda args: Short().dispatch(args)
    }
}

