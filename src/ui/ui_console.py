from typing import Literal
from colorama import Fore as fg

# core
from core import settings


class Colors:
    """Esquema de cores da ferramenta"""

    # Alertas
    SUCCESS = fg.GREEN
    ERROR = fg.RED
    WARNING = fg.YELLOW
    INFO = fg.BLUE

    # UI
    FG_ONE = fg.RED
    FG_TWO = fg.WHITE

    # Texto
    TEXT_ONE = fg.RED
    TEXT_TWO = fg.WHITE



def list_commands(name: str, cmds: dict):
    """Exibe de forma organizada os comandos passados no [cmds]"""

    print()
    for cmd, data in cmds.items():
        print(f"{Colors.SUCCESS}{cmd}{Colors.TEXT_TWO}: {data['desc']}")


def alert(
    type_: Literal['success', 'error', 'warning', 'info'],
    text: str
):
    """Alerta padronizado"""

    type_ = type_.lower()

    types = {
        'success': Colors.SUCCESS,
        'error': Colors.ERROR,
        'warning': Colors.WARNING,
        'info': Colors.INFO
    }

    FG_ALERT = types.get(type_, Colors.INFO)

    print(f"\n{FG_ALERT}[{type_.upper()}] {Colors.TEXT_TWO}{text}")


class Banners:
    TOOL_LOGO = f"""{Colors.FG_ONE}
                            ┏┓┳┓┏┓┳┳┓┏┓┏┳┓┓┏┏┓┳┳┏┓
                            ┃┃┣┫┃┃┃┃┃┣  ┃ ┣┫┣ ┃┃┗┓
                            ┣┛┛┗┗┛┛ ┗┗┛ ┻ ┛┗┗┛┗┛┗┛
                       Developed by {Colors.FG_TWO}{settings.AUTHOR} {Colors.FG_ONE}- ver. {Colors.FG_TWO}{settings.VERSION}"""
