import subprocess, sys

# core
from core.exceptions import MissingArgumentsError



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

    print()
    entries = input(" > ")

    if not entries:
        raise MissingArgumentsError("Nenhuma entrada foi informada")

    return entries.split()


def shutdown():
    """Finaliza a ferramenta"""

    sys.exit()

