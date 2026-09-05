

class CommandNotFoundError(Exception):
    def __init__(self, command: str):
        super().__init__(f"{command}: comando não encontrado")


class MissingArgumentsError(Exception):
    pass


class PathNotFoundError(Exception):
    def __init__(self, path):
        super().__init__(f"{path}: não existe, verifique o caminho e não esqueça que deve ser o caminho absoluto")

