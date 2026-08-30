

class CommandNotFoundError(Exception):
    def __init__(self, message):
        super().__init__(message + ": comando não encontrado")


class FolderNotFoundError(Exception):
    def __init__(self, message):
        super().__init__(message + ": pasta não encontrada")

