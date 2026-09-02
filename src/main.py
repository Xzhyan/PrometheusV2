
# core
from core import settings
from core.dependencies import check_dependencies
from core.exceptions import MissingArgumentsError, CommandNotFoundError

# utils
from utils.system import entry, set_title

# ui
from ui.ui_console import alert, Banners

# commands
from commands.general import shutdown, clear, DEFAULT_COMMANDS


class Prometheus:
    def __init__(self):
        self.running: bool = True # controle do loop principal

    def startup(self):
        """Definições iniciais"""

        clear()
        set_title(title=settings.TOOL_NAME)
        print(Banners.TOOL_LOGO)

        if not check_dependencies():
            raise KeyboardInterrupt

        self.dispatch()

    def dispatch(self):
        """Tratamento dos comandos da ferramenta"""

        while self.running:
            try:
                args = entry()
                cmd = args[0]

                if cmd in DEFAULT_COMMANDS:
                    DEFAULT_COMMANDS[cmd]['handler']()

                else:
                    raise CommandNotFoundError(command=cmd)

            except CommandNotFoundError as e:
                alert('error', str(e))

            except MissingArgumentsError as e:
                alert('error', str(e))

            except Exception as e:
                alert('error', str(e))



if __name__ == '__main__':
    try:
        tool = Prometheus()
        tool.startup()

    except KeyboardInterrupt:
        alert('info', "Finalizando...")
        shutdown()
