import subprocess

# core
from core.config import BASE_DIR


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


