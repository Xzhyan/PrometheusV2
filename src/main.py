
# ui
from ui.ui_console import alert

# utils
from utils.console import entry, shutdown, clear


class Main:
    def __init__(self):
        self.running = True

    def startup(self):
        clear()

        self.dispatch()

    def dispatch(self):
        """Trata os comandos da ferramenta"""

        while self.running:
            try:
                entries = entry()

            except ValueError as e:
                alert('error', str(e))

            except Exception as e:
                alert('error', str(e))


if __name__ == "__main__":
    try:
        prometheus = Main()
        prometheus.startup()

    except KeyboardInterrupt:
        alert('info', "Finalizando ferramenta...", True)
        shutdown()
