
# core
from core import settings
from core.dependencies import check
from core.exceptions import CommandNotFoundError

# utils
from utils.system import clear, set_title, entry

# ui
from ui.ui_console import alert, Banners

# commands
from commands.defaults import CATEGORIES, DEFAULT_CMDS


class Main:
    def __init__(self):
        self.running: bool = True # controla o loop principal

    def startup(self):
        clear()
        set_title(settings.TOOL_NAME)
        print(Banners.TOOL_LOGO)

        if check(): # verificador de dependencias
            self.dispatch()

    def dispatch(self):
        """Trata os comandos"""

        while self.running:
            try:
                entries = entry()
                command = entries[0]

                if command in CATEGORIES:
                    CATEGORIES[command]['handler'](entries)

                elif command in DEFAULT_CMDS:
                    DEFAULT_CMDS[command]['handler'](entries)

                else:
                    raise CommandNotFoundError(command)

            except CommandNotFoundError as e:
                alert('error', str(e))

            except ValueError as e:
                alert('error', str(e))


if __name__ == '__main__':
    try:
        tool = Main()
        tool.startup()

    except KeyboardInterrupt:
        alert('info', "Finalizando...")

