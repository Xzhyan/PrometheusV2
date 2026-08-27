# utils
from utils.console import shutdown, restart, clear



DEFAULT_COMMANDS = {
    'exit': {
        'desc': "Finaliza a ferramenta",
        'handler': shutdown
    },
    'restart': {
        'desc': "Reinicia a ferramenta",
        'handler': restart
    },
    'clear': {
        'desc': "Limpa a tela da ferramenta",
        'handler': clear
    }
}
