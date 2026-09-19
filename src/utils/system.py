import subprocess, sys

# ui
from ui.ui_console import Colors


def shell_cmd(cmd: str):
    """Executa comandos nativos do terminal"""

    subprocess.run(cmd, shell=True)


def shutdown():
    """Finaliza a ferramenta"""

    sys.exit()


def clear():
    """Limpa a tela da ferramenta"""

    shell_cmd('cls')


def set_title(text: str):
    """Seta titulo ao terminal"""

    shell_cmd(f'title {text}')


def entry() -> list[str]:
    """Recebe as entradas do usuário"""

    entries = input("\n > ")

    if not entries:
        raise ValueError("você precisa informar um comando válido!")

    entries = entries.lower() # normaliza para evitar entradas em upper case

    return entries.split()


def list_commands(name: str, cmd_dict: dict):
    """Organiza a listagem dos comandos e exibe na tela"""

    print(f"\n{Colors.FG_ONE}─────[ {Colors.TEXT_TWO}{name} {Colors.TEXT_ONE}]─────")

    for cmd, data in cmd_dict.items():
        print(f"{Colors.FG_ONE}┌─[ {Colors.SUCCESS}{cmd}")
        print(f"{Colors.FG_ONE}├─ {Colors.TEXT_THREE}description: {Colors.TEXT_TWO}{data['desc']}")
        print(f"{Colors.FG_ONE}└─ {Colors.TEXT_THREE}usage: {Colors.TEXT_TWO}{data['usage']}")

