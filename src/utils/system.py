import subprocess

# ui
from ui.ui_console import Colors


def shell_cmd(command):
    """Executa comandos do terminal"""

    subprocess.run(command, shell=True)


def clear():
    """Limpa a tela da ferramenta"""

    shell_cmd("cls")


def entry():
    """Recebe as entradas da ferramenta"""

    entries = input(" > ")
    normalized = entries.lower()

    return normalized.split()


