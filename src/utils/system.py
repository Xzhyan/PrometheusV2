import subprocess


def shell_cmd(cmd):
    """Executa comandos nativos do terminal"""

    subprocess.run(cmd, shell=True)


def clear():
    """Limpa a tela da ferramenta"""

    shell_cmd('cls')


def set_title(text):
    """Seta titulo ao terminal"""

    shell_cmd(f'title {text}')


def entry():
    """Recebe as entradas do usuário"""

    entries = input(" > ")

    if not entries:
        raise ValueError("você precisa informar um comando válido!")

    entries = entries.lower() # normaliza para evitar entradas em upper case

    return entries.split()
