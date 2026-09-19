
class CommandNotFoundError(Exception):
    def __init__(self, command):
        super().__init__(f"{command}: comando não encontrado!")

