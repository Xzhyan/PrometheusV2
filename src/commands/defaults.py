

# utils
from utils.system import shutdown, clear, list_commands


def show_default_cmds():
    """Exibe os comandos normais"""

    list_commands("Comandos Normais", DEFAULT_CMDS)


CATEGORIES: dict = {
    'defaults': {
        'desc': "Exibe a lista de comandos normais",
        'usage': "defaults",
        'handler': show_default_cmds
    },
}


def help_menu():
    """Exibe o menu de ajuda e comandos da ferramenta"""

    list_commands("Categorias de Comandos", CATEGORIES)


DEFAULT_CMDS: dict = {
    'exit': {
        'desc': "Finaliza a ferramenta",
        'usage': "exit",
        'handler': shutdown
    },
    'clear': {
        'desc': "Limpa a tela da ferramenta",
        'usage': "clear",
        'handler': clear
    },
    'help': {
        'desc': "Exibe o menu de ajuda",
        'usage': "help",
        'handler': help_menu
    },
    'restart': {
        'desc': "Reinicia a ferramenta",
        'usage': "restart",
        'handler': "restart"
    }
}

