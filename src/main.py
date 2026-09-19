
# core
from core import settings

# utils
from utils.system import clear, set_title, entry

# ui
from ui.ui_console import alert, Banners


class Main:
    def __init__(self):
        self.running: bool = True # controla o loop principal

    def startup(self):
        clear()
        set_title(settings.TOOL_NAME)
        print(Banners.TOOL_LOGO)

        self.dispatch()

    def dispatch(self):
        """Trata os comandos"""

        while self.running:
            try:
                entries = entry()
                command = entries[0]

                print(command)


            except ValueError as e:
                alert('error', str(e))


if __name__ == '__main__':
    try:
        tool = Main()
        tool.startup()

    except KeyboardInterrupt:
        alert('info', "Finalizando...")