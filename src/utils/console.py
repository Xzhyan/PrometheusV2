import subprocess, sys

# core
from core import settings, Colors

# utils
from .functions import run_py_module


def entry():
    """Recebe entradas do usuário e retorna em argumentos separados"""

    print(f"\n {Colors.FG_ONE}┌─({Colors.TEXT_TWO}{settings.TOOL_NAME}{Colors.FG_ONE})-[{Colors.FG_ONE}]")
    entries = input(f" {Colors.FG_ONE}└───[> {Colors.TEXT_TWO}")

    if not entries:
        raise ValueError("Você precisa informar um comando válido")

    return entries.split()


def shell_cmd(cmd):
    """Usa o subprocess para executar comandos simples no cmd"""

    try:
        subprocess.run(cmd, shell=True)

    except Exception as e:
        print(str(e))


def clear():
    """Limpa a tela CLI da ferramenta"""

    shell_cmd('cls')


def shutdown():
    """Fecha a ferramenta"""

    sys.exit(0)


def restart():
    """Reinicia a ferramenta"""

    run_py_module(r'src\main.py')


def set_title(title):
    """Define um titulo ao prompt"""

    shell_cmd(f'title {title}')
