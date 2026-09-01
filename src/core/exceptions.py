

class CommandNotFoundError(Exception):
    def __init__(self, command: str):
        super().__init__(f"{command}: comando não encontrado")


class MissingArgumentsError(Exception):
    pass
