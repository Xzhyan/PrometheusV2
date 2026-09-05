import json
from pathlib import Path


def read_json(path: Path) -> dict:
    """Lê o arquivo json especificado (path)"""

    with open(path, 'r', encoding='utf-8') as file:
        data = json.load(file)

    return data


def write_json(path: Path, data: dict):
    """Escreve dados no arquivo json (path)"""

    with open(path, 'w', encoding='utf-8') as file:
        json.dump(data, file, indent=4, ensure_ascii=False)




