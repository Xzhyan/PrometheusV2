from pathlib import Path

# core
from core.constants import SHORTS_JSON

# utils
from utils.system import shutdown, clear, restart, shell_popen, list_commands
from utils.functions import read_json, write_json

# ui
from ui.ui_console import alert, Colors


def show_default_cmds(*args):
    """Exibe os comandos normais"""

    list_commands("Comandos Normais", DEFAULT_CMDS)


CATEGORIES: dict = {
    'defaults': {
        'desc': "Exibe a lista de comandos normais",
        'usage': "defaults",
        'handler': show_default_cmds
    },
}


def help_menu(*args):
    """Exibe o menu de ajuda e comandos da ferramenta"""

    list_commands("Categorias de Comandos", CATEGORIES)


class Open:
    """Abre o explorer, code ou aplicativo por meio do atalho"""

    def __init__(self):
        self.shorts = read_json(SHORTS_JSON)

        self.SUBCOMMANDS: dict = {
            'help': {
                'desc': "exibe o menu de ajuda do comando",
                'usage': "open help",
                'handler': self.help
            },
            'code': {
                'desc': "abre o vs code no path do atalho",
                'usage': "open code nome_do_atalho",
                'handler': lambda path: self.code(path)
            },
            'explorer': {
                'desc': "abre o explorer na path do atalho",
                'usage': "open explorer nome_do_atalho",
                'handler': lambda path: self.explorer(path)
            },
            'app': {
                'desc': "abre o atalho se for um aplicativo",
                'usage': "short remove",
                'handler': lambda path: self.app(path)
            }
        }

    def help(self):
        list_commands("open", self.SUBCOMMANDS)

    def code(self, path: Path):
        try:
            shell_popen(f"code {path}")

        except Exception as e:
            alert('error', str(e))

    def explorer(self, path: Path):
        try:
            shell_popen(f"explorer {path}")

        except Exception as e:
            alert('error', str(e))

    def app(self, path: Path):
        try:
            shell_popen(f"start {path}")

        except Exception as e:
            alert('error', str(e))

    def dispatch(self, args: list[str]):
        if len(args) < 2:
            raise ValueError("argumento faltando, tente: open help")

        cmd = args[1]

        if args[1] == 'help':
            self.SUBCOMMANDS[cmd]['handler']()

        elif cmd in self.SUBCOMMANDS:
            short_name = args[2]

            try:
                if cmd == 'code' or cmd == 'explorer':
                    path = self.shorts['dir'][short_name]

                elif cmd == 'app':
                    path = self.shorts['app'][short_name]

                if not path:
                    raise KeyError()

                self.SUBCOMMANDS[cmd]['handler'](path)

            except KeyError:
                alert('error', f"{short_name}: o atalho não existe!")

            except KeyboardInterrupt:
                alert('info', "comando open finalizado.")

        else:
            raise ValueError("comando inexistente, tente: open help")


class Short:
    """Comando de atalhos"""

    def __init__(self):
        self.shorts = read_json(SHORTS_JSON) # atalhos já adicionados no json

        # dict de subcomandos do comando short
        self.SUBCOMMANDS: dict = {
            'help': {
                'desc': "exibe o menu de ajuda do comando",
                'usage': "short help",
                'handler': self.help
            },
            'add': {
                'desc': "adiciona um atalho",
                'usage': "short add",
                'handler': self.add
            },
            'list': {
                'desc': "lista todos os atalhos",
                'usage': "short list",
                'handler': self.list
            },
            'remove': {
                'desc': "remove um atalho",
                'usage': "short remove",
                'handler': self.remove
            }
        }

        self.types = ['app', 'dir']

    def help(self):
        list_commands("short", self.SUBCOMMANDS)

    def add(self):
        while True:
            type_ = input(f"     {Colors.FG_ONE}●▸ {Colors.TEXT_TWO}tipo do atalho (app/dir): ")

            if type_ in self.types:
                break

            alert('info', "escolha o tipo de atalho: app/dir")

        while True:
            name = input(f"     {Colors.FG_ONE}●▸ {Colors.TEXT_TWO}nome do novo atalho: ")
            path = input(f"     {Colors.FG_ONE}●▸ {Colors.TEXT_TWO}path absoluto do atalho: ")

            if type_ and name and path:
                break

            alert('info', "nenhum campo pode ser vazio!")

        # verifica se o atalho já existe
        if name in self.shorts[type_]:
            raise ValueError("o atalho já existe, tente: short list")

        # adicionar atalho
        self.shorts[type_][name] = path
        write_json(SHORTS_JSON, self.shorts)

        alert('success', f"{name}: atalho adicionado com sucesso!")

    def list(self):
        for short, data in self.shorts.items():
            if len(data) >= 1:
                print(f"\n{Colors.FG_ONE}●─────[ {Colors.SUCCESS}{short} {Colors.TEXT_ONE}]─────●")
                
                for name in data:
                    print(f"{Colors.FG_ONE} ●▸ {Colors.TEXT_TWO}{name}")

    def remove(self):
        while True:
            name = input(f"     {Colors.FG_ONE}●▸ {Colors.TEXT_TWO}nome do atalho que deseja remover: ")

            if name:
                break

            alert('info', "você precisa informar um nome para o atalho")

        # verifica se o atalho existe
        for type_ in self.types:
            if name in self.shorts[type_]:
                del self.shorts[type_][name]
                write_json(SHORTS_JSON, self.shorts)

                alert('success', f"{name}: atalho removido com sucesso!")
                return

        raise ValueError("o atalho não existe ou já foi removido!")

    def dispatch(self, args: list[str]):
        if len(args) <= 1:
            raise ValueError("argumento faltando, tente: short help")

        cmd = args[1]

        if cmd in self.SUBCOMMANDS:
            try:
                self.SUBCOMMANDS[cmd]['handler']()

            except KeyboardInterrupt:
                alert('info', "comando short finalizado.")

        else:
            raise ValueError("comando inexistente, tente: short help")


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
        'handler': restart
    },
    'short': {
        'desc': "Atalhos personalizadios",
        'usage': "short help",
        'handler': lambda args: Short().dispatch(args)
    },
    'open': {
        'desc': "Abre os atalhos adicionados",
        'usage': "open help",
        'handler': lambda args: Open().dispatch(args)
    },
}

