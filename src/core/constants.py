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
            'name': "Virus Total",
            'desc': "Útil para verificar arquivos, urls e fazer pesquisas",
            'url': "https://www.virustotal.com/gui/home/upload"
        },
        'url_checker': {
            'name': "Bitdefender Link Checker",
            'desc': "Use para verificar links/urls suspeitas",
            'url': "https://www.bitdefender.com/pt-br/consumer/link-checker"
        },
        'email_pwned': {
            'name': "Have I Been Pwned",
            'desc': "Verifique se seus emails estão seguros",
            'url': "https://haveibeenpwned.com/"
        }
    },
    'vpns': {
        'proton_vpn': {
            'name': "Proton VPN",
            'desc': "Possuí VPN gratuita, basta baixar e instalr o App",
            'url': "https://protonvpn.com/pt-br"
        }
    },
    'others': {
        'patorjk': {
            'name': "Patorjk.com",
            'desc': "Gerador de texto em ASCII",
            'url': "https://patorjk.com/software/taag"
        }
    }
}
