import subprocess, sys

# core
from core import settings
from core.constants import CURRENT_USER
from core.exceptions import MissingArgumentsError

# ui
from ui.ui_console import Colors



def shell_cmd(command: str):
    """Usa o subprocess para executar comandos do terminal"""

    subprocess.run(command, shell=True)


def set_title(title: str):
    """Define o titulo do terminal"""

    shell_cmd(command=f"title {title}")


def clear():
    """Limpa a tela da ferramenta"""

    shell_cmd(command="cls")


def entry() -> list[str]:
    """Recebe entradas do usuário no CLI"""

    print(f"\n {Colors.FG_ONE}┌─({Colors.FG_TWO}{settings.TOOL_NAME.lower()}{Colors.FG_ONE})─[{Colors.FG_TWO}{CURRENT_USER}{Colors.FG_ONE}]")
    entries = input(f" {Colors.FG_ONE}└───[ {Colors.FG_TWO}")

    if not entries:
        raise MissingArgumentsError("Nenhuma entrada foi informada")

    return entries.split()


def shutdown():
    """Finaliza a ferramenta"""

    sys.exit()

