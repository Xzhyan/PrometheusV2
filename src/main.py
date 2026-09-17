
# utils
from utils.system import clear, entry

# ui
from ui.ui_console import Banners, alert


class Main:
    def __init__(self):
        self.running: bool = True

    def startup(self):
        clear()
        print(Banners.TOOL_LOGO)

        self.dispatch()

    def dispatch(self):
        while self.running:
            try:
                entries = entry()

            except Exception as e:
                print(str(e))


if __name__ == '__main__':
    try:
        tool = Main()
        tool.startup()

    except KeyboardInterrupt:
        alert('info', "Finalizando...")
