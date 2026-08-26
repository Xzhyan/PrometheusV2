import subprocess, sys


def entry():
    """Recebe entradas do usuário e retorna em argumentos separados"""

    entries = input(" > ")

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

    pass
