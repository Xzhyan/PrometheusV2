
# core
from core import settings
from core.exceptions import CommandNotFound

# ui
from ui.ui_console import alert
from ui.banners import Banners

# utils
from utils.console import entry, shutdown, clear, set_title

# commands
from cmds import Help, DEFAULT_COMMANDS


class Main:
    def __init__(self):
        self.running = True # controle de execução do loop principal
        self.help = Help() # Menu de ajuda

    def startup(self):
        clear()
        set_title(settings.TOOL_NAME)
        print(Banners.TOOL_LOGO)

        self.dispatch()

    def dispatch(self):
        """Trata os comandos da ferramenta"""

        while self.running:
            try:
                entries = entry()
                command = entries[0] # primeiro arg é o comando

                if command == 'help':
                    self.help.show_help()

                elif command in DEFAULT_COMMANDS:
                    DEFAULT_COMMANDS[command]['handler']()

                else:
                    raise CommandNotFound(command)

            except CommandNotFound as e:
                alert('error', str(e))

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
