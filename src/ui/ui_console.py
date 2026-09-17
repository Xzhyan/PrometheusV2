from colorama import Fore as fg


class Colors:
    """Esquema de cores da ferramenta"""

    # Tool
    FG_ONE = fg.RED
    FG_TWO = fg.LIGHTWHITE_EX

    # Text
    TEXT_ONE = fg.RED
    TEXT_TWO = fg.LIGHTWHITE_EX

    # Alerts
    SUCCESS = fg.GREEN
    ERROR = fg.RED
    WARNING = fg.YELLOW
    INFO = fg.BLUE


class Banners:
    TOOL_LOGO = f"""{Colors.FG_ONE}
                    ┏┓┳┓┏┓┳┳┓┏┓┏┳┓┓┏┏┓┳┳┏┓
                    ┃┃┣┫┃┃┃┃┃┣  ┃ ┣┫┣ ┃┃┗┓
                    ┣┛┛┗┗┛┛ ┗┗┛ ┻ ┛┗┗┛┗┛┗┛
    """


def alert(type_, text):
    """Alerta personalizado"""

    type_ = type_.lower() # normaliza para evitar problemas com o dict

    types: dict = {
        'success': Colors.SUCCESS,
        'error': Colors.ERROR,
        'warning': Colors.WARNING,
        'info': Colors.INFO
    }

    FG_ALERT = types.get(type_, Colors.TEXT_TWO)

    print(f"{FG_ALERT}[{type_.upper()}] {Colors.TEXT_TWO}{text}")
