
# core
from core import settings
from core.exceptions import MissingArgumentsError

# utils
from utils.system import entry, clear, set_title, shutdown

# ui
from ui.ui_console import alert


class Prometheus:
    def __init__(self):
        self.running: bool = True # controle do loop principal

    def startup(self):
        """Definições iniciais"""

        clear()
        set_title(title=settings.TOOL_NAME)
 
        self.dispatch()

    def dispatch(self):
        """Tratamento dos comandos da ferramenta"""

        while self.running:
            try:
                args = entry()


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
