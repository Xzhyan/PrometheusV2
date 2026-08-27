
# core
from core import Colors


def alert(type_, text, br_line = None):
    """Exibe alertas padronizados no CLI"""

    type_ = type_.lower() # normaliza pra evitar problemas

    alert_types = {
        'info': Colors.INFO,
        'success': Colors.SUCCESS,
        'error': Colors.ERROR,
        'warning': Colors.WARNING
    }

    FG_ALERT = alert_types.get(type_, Colors.INFO)

    # Usa um print para simular uma quebra de linha do CLI
    if br_line:
        print()

    print(f"{FG_ALERT}[> {type_.upper()} <] {Colors.TEXT_TWO}{text}")

