from json import JSONDecodeError
from pathlib import Path

# core
from core.constants import JSON_FILE
from core.exceptions import CommandNotFoundError, MissingArgumentsError, PathNotFoundError

# utils
from utils.system import shutdown, clear
from utils.functions import read_json, write_json

# ui
from ui.ui_console import alert, list_commands


def help(*args):
    """Exibe o menu de ajuda e lista de comandos"""

    print("\nBem-vindo ao menu de ajuda da ferramenta")

    list_commands(name="Comandos Normais", cmds=DEFAULT_COMMANDS)


def interrupt(*args):
    """Usa o KeyboardInterrupt para finalizar a ferramenta"""

    # No except KeyboardInterrupt a função 'shutdown' é chamada pra finalizar corretamente
    raise KeyboardInterrupt


class CustomShort:
    def __init__(self, args: list[str]):
        if not len(args) >= 2:
            raise MissingArgumentsError("o comando short usa mais algumentos: add, remove, list")
        
        cmd = args[1] # segundo argumento dos args é o comando dentro de short [add, remove, list]

        self.manage(cmd)

    def list_(self) -> dict:
        data: dict = {}

        try:
            data = read_json(path=JSON_FILE)

        except FileNotFoundError:
            alert('error', f"o aquivo {JSON_FILE} não existe")

        except JSONDecodeError as e:
            alert('error', str(e))

        return data

    def remove(self):
        print("ok")

    def save(self):
        types = ['app', 'dir']

        type_ = input("\n > informe o tipo de atalho [app/dir]: ")

        if not type_ in types:
            alert('info', "precisa ser do tipo 'app' ou 'dir'")
            self.save()

        name = input(" > nome ou apelido para o atalho: ")

        if not name:
            alert('info', "um nome deve ser informado")
            self.save()

        path: Path = Path(input(" > caminho do atalho: "))

        if not path:
            alert('info', "um caminho deve ser informado")
            self.save()

        data = self.list_()

        for t, data in data.items():
            if not name in data['name']:
                print('ok')

    def manage(self, cmd):
        """Controla os sub comandos do comando de atalhos"""

        CMDS = {
            'add': {
                'desc': "adicionar um novo atalho",
                'handler': self.save
            },
            'remove': {
                'desc': "remover um atalho",
                'handler': self.remove
            },
            'list': {
                'desc': "listar os atalhos adicionados",
                'handler': self.list_
            }
        }

        if cmd in CMDS:
            CMDS[cmd]['handler']()

        else:
            raise CommandNotFoundError(command=f"short -> {cmd}")



DEFAULT_COMMANDS = {
    'exit': {
        'desc': "finalizar a ferramenta",
        'handler': interrupt
    },
    'help': {
        'desc': "exibe o menu de ajuda",
        'handler': help
    },
    'clear': {
        'desc': "limpa a tela da ferramenta",
        'handler': clear
    },
    'short': {
        'desc': "atalhos personalizados",
        'handler': lambda args: CustomShort(args)
    }
}

