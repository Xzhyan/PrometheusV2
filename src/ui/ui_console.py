from colorama import Fore as fg

# core
from core import settings


class Colors:
    """Esquema de cores"""

    # tool
    FG_ONE = fg.RED
    FG_TWO = fg.LIGHTWHITE_EX

    # text
    TEXT_ONE = fg.RED
    TEXT_TWO = fg.LIGHTWHITE_EX
    TEXT_THREE = fg.WHITE

    # alerts
    SUCCESS = fg.GREEN
    ERROR = fg.RED
    WARNING = fg.YELLOW
    INFO = fg.BLUE


class Banners:
    TOOL_LOGO = f"""{Colors.TEXT_ONE}
                               ┏┓┳┓┏┓┳┳┓┏┓┏┳┓┓┏┏┓┳┳┏┓
                               ┃┃┣┫┃┃┃┃┃┣  ┃ ┣┫┣ ┃┃┗┓
                               ┣┛┛┗┗┛┛ ┗┗┛ ┻ ┛┗┗┛┗┛┗┛
                        {Colors.TEXT_TWO}Developed by {Colors.TEXT_ONE}{settings.AUTHOR} {Colors.TEXT_TWO}- version: {Colors.TEXT_ONE}{settings.VERSION}"""


def alert(type_: str, text: str):
    """Mensagem de alerta padronizada"""

    types = {
        'success': Colors.SUCCESS,
        'error': Colors.ERROR,
        'warning': Colors.WARNING,
        'info': Colors.INFO
    }

    FG_ALERT = types.get(type_.lower(), Colors.TEXT_TWO)

    print(f"\n{FG_ALERT}[{type_.upper()}] {Colors.TEXT_TWO}{text}")
