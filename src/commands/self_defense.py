from pathlib import Path

# core
from core.constants import URL_JSON

# utils
from utils.system import list_commands
from utils.functions import read_json


def url_dispatch(categories: list) -> dict:

    ALL_URLS: dict = {}

    urls = read_json(URL_JSON)

    for category in categories:
        for options, data in urls.items():
            if category in options:
                print(data)


    #         ALL_URLS.update(data)

    # return ALL_URLS


# def url_dispatch(category = None) -> dict:
#     """Orgaiza as urls do urls.json para uso de comandos"""
    
#     urls = read_json(URL_JSON)

#     for options, data in urls.items():
#         if category == None:
#             return urls # usado apenas para executar os comandos de url

#         elif category in options:
#             return data # usado apenas para quando for preciso exibir a lista de urls por categoria


ALL_URLS: dict = url_dispatch(['checkers', 'vpns', 'others'])


def open_browser_url(url):
    print(url)


def checkers(*args):
    URLS = url_dispatch(['vpns'])

    # list_commands("Checkers", URLS)


SELF_DEFENSE = {
    'checkers': {
        'desc': "Verificação de arquivos, links e emails",
        'usage': "checkers",
        'handler': checkers
    }
}
