# utils
from utils.console import shutdown, restart, clear



class Short:
    def __init__(self, args):
        pass

    def add(self):
        """Adiciona um atalho"""

        pass



DEFAULT_COMMANDS = {
    'exit': {
        'desc': "finaliza a ferramenta",
        'handler': shutdown
    },
    'restart': {
        'desc': "reinicia a ferramenta",
        'handler': restart
    },
    'clear': {
        'desc': "limpa a tela da ferramenta",
        'handler': clear
    },
    'short': {
        'desc': "atalhos personalizados",
        'handler': lambda args: Short(args)
    }
}
