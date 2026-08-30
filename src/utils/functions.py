import os, subprocess, time

# core
from core.config import BASE_DIR
from core.exceptions import FolderNotFoundError

# ui
from ui.ui_console import alert


def run_py_module(path, new_window=False):
    """
    Executa um scrip/modulo python separadamente
    Apenas scripts dentro do mesmo BASE_DIR
    """

    venv = BASE_DIR / '.venv' / 'Scripts' / 'python.exe'
    script = BASE_DIR / path

    if new_window:
        subprocess.Popen([venv, script], creationflags=subprocess.CREATE_NEW_CONSOLE)

    subprocess.run([venv, script], check=True)


def create_folder(folder_path):
    """Cria a pasta conforme o path especificado"""

    try:
        alert('info', f"criando: {folder_path}")

        time.sleep(0.5)
        os.mkdir(folder_path)
        time.sleep(0.5)

        alert('success', f"{folder_path}: criado!")

    except Exception as e:
        alert('error', str(e))


def check_file(file_path):
    """Verifica existência do arquivo especificado"""

    alert('info', f"verificando: {file_path}")

    if not os.path.isfile(file_path):
        raise FileNotFoundError(f"{file_path}: arquivo não encontrado")

    time.sleep(0.5)
    alert('success', f"{file_path}: OK!")
    time.sleep(0.5)

    return True


def check_folder(folder_path, create=False):
    """Verifica existência da pasta especificada"""

    alert('info', f"verificando: {folder_path}")

    if not os.path.isdir(folder_path):
        if create:
            create_folder(folder_path)

        else:
            raise FolderNotFoundError(folder_path)

    time.sleep(0.5)
    alert('success', f"{folder_path}: OK!")
    time.sleep(0.5)

    return True

