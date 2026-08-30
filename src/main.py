
# core
from core import settings
from core.dependencies import check_dependencies
from core.exceptions import CommandNotFoundError

# ui
from ui.ui_console import alert
from ui.banners import Banners

# utils
from utils.console import entry, shutdown, clear, set_title

# commands
from cmds import show_help, DEFAULT_COMMANDS


class Main:
    def __init__(self):
        self.running = True # controle de execução do loop principal

    def startup(self):
        if check_dependencies(): # Só abre a ferramenta dps da verificação
            clear()
            set_title(settings.TOOL_NAME)
            print(Banners.TOOL_LOGO)
            self.dispatch()

        else:
            shutdown

    def dispatch(self):
        """Trata os comandos da ferramenta"""

        while self.running:
            try:
                entries = entry()
                command = entries[0] # primeiro arg é o comando

                if command == 'help':
                    show_help()

                elif command in DEFAULT_COMMANDS:
                    DEFAULT_COMMANDS[command]['handler']()

                else:
                    raise CommandNotFoundError(command)

            except CommandNotFoundError as e:
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
