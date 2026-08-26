

def alert(type_, text, br_line = None):
    """Exibe alertas padronizados no CLI"""

    type_ = type_.upper()

    # Usa um print para simular uma quebra de linha do CLI
    if br_line:
        print()

    print(f"[{type_}] >> {text}")

