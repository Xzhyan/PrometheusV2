
# utils
from utils.system import shutdown, clear


def list_commands(name: str, cmds: dict):
    """Exibe de forma organizada os comandos passados no [cmds]"""

    print()
    for cmd, data in cmds.items():
        print(f"{cmd}: {data['desc']}")


def help(*args):
    """Exibe o menu de ajuda e lista de comandos"""

    print("\nBem-vindo ao menu de ajuda da ferramenta")

    list_commands(name="Comandos Normais", cmds=DEFAULT_COMMANDS)


def interrupt(args):
    """Usa o KeyboardInterrupt para finalizar a ferramenta"""

    # No except KeyboardInterrupt a função 'shutdown' é chamada pra finalizar corretamente
    raise KeyboardInterrupt


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
    }
}

