from pathlib import Path


# camingo absoluto
BASE_DIR = Path(__file__).resolve().parent.parent.parent

# Caminho do laucher .bat
BAT_LAUNCHER = BASE_DIR / 'prometheus.bat'

# Pasta de dados
DATA_DIR = BASE_DIR / 'data'

# Arquivo de atalhos do sistema
SHORTS_JSON = DATA_DIR / 'shorts.json'

# Arquivo de links e urls
URL_JSON = DATA_DIR / 'urls.json'

# Dicionário de links/urls padrões da ferramenta
URL_DICT: dict = {
    'checkers': {
        'virus_total': {
            'desc': "Útil para verificar arquivos, urls e fazer pesquisas",
            'usage': "virus_total",
            'handler': "https://www.virustotal.com/gui/home/upload"
        },
        'url_checker': {
            'desc': "Use para verificar links/urls suspeitas",
            'usage': "url_checker",
            'handler': "https://www.bitdefender.com/pt-br/consumer/link-checker"
        },
        'email_pwned': {
            'desc': "Verifique se seus emails estão seguros",
            'usage': "email_pwned",
            'handler': "https://haveibeenpwned.com/"
        }
    },
    'vpns': {
        'proton_vpn': {
            'desc': "Possuí VPN gratuita, basta baixar e instalr o App",
            'usage': "proton_vpn",
            'handler': "https://protonvpn.com/pt-br"
        }
    },
    'others': {
        'patorjk': {
            'desc': "Gerador de texto em ASCII",
            'usage': "patorjk",
            'handler': "https://patorjk.com/software/taag"
        }
    }
}
