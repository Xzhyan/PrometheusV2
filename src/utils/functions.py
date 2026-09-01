import subprocess, time, json
from pathlib import Path

# core
from core.config import BASE_DIR
from core.exceptions import FolderNotFoundError

# ui
from ui.ui_console import alert


def run_py_module(path: Path, new_window: bool = False):
    """
    Executa um scrip/modulo python separadamente
    Apenas scripts dentro do mesmo BASE_DIR
    """

    venv = BASE_DIR / '.venv' / 'Scripts' / 'python.exe'
    script = BASE_DIR / path

    if new_window:
        subprocess.Popen([venv, script], creationflags=subprocess.CREATE_NEW_CONSOLE)

    else:
        subprocess.run([venv, script], check=True)


def create_folder(folder_path: Path):
    """Cria a pasta conforme o path especificado"""

    alert('info', f"criando: {folder_path}")

    time.sleep(0.5)
    folder_path.mkdir(parents=True, exist_ok=True)
    time.sleep(0.5)

    alert('success', f"{folder_path}: criado!")


def check_file(file_path: Path) -> bool:
    """Verifica existência do arquivo especificado"""

    alert('info', f"verificando: {file_path}")

    if not file_path.is_file():
        raise FileNotFoundError(f"{file_path}: arquivo não encontrado")

    time.sleep(0.5)
    alert('success', f"{file_path}: OK!")
    time.sleep(0.5)

    return True


def check_folder(folder_path: Path, create: bool = False) -> bool:
    """Verifica existência da pasta especificada"""

    alert('info', f"verificando: {folder_path}")

    if not folder_path.is_dir():
        if create:
            create_folder(folder_path)

        else:
            raise FolderNotFoundError(folder_path)

    time.sleep(0.5)
    alert('success', f"{folder_path}: OK!")
    time.sleep(0.5)

    return True


def read_json(path: Path) -> dict:
    """Lê um arquivo json"""

    with open(path, 'r', encoding='utf-8') as file:
        data = json.load(file)

    return data


def write_json(path: Path, data: dict):
    """Escreve dados no arquivo json"""

    with open(path, 'w', encoding='utf-8') as file:
        json.dump(data, file, indent=4, ensure_ascii=False)
