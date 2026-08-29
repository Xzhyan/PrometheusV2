# core
from core import Colors

# commands
from .defaults import DEFAULT_COMMANDS


def list_commands(name, cmd_list):
    """Separa e lista os comandos"""

    print("") # print vazio para por um espaço entre comandos

    for cmd, data in cmd_list.items():
        print(f"{Colors.SUCCESS}{cmd}{Colors.TEXT_TWO}: {data['desc']}")


class Help:
    def __init__(self):
        pass

    def show_help(self):
        """Menu de ajuda da ferramenta"""

        list_commands("Comandos Normais", DEFAULT_COMMANDS)


