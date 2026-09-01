

class CommandNotFoundError(Exception):
    def __init__(self, message: str):
        super().__init__(message + ": comando não encontrado")


class FolderNotFoundError(Exception):
    def __init__(self, message: str):
        super().__init__(message + ": pasta não encontrada")


class MissingArgumentError(Exception):
    def __init__(self):
        super().__init__("Argumentos faltando, verifique o modo de uso do comando")


