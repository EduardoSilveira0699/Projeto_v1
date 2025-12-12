def ler_int(prompt: str) -> int:
    """
    Lê um inteiro do usuário com tratamento de erro.
    Continua pedindo até obter um inteiro válido.
    """
    while True:
        val = input(prompt).strip()
        if not val:
            print("Valor obrigatório.")
            continue
        try:
            return int(val)
        except ValueError:
            print("Digite um número inteiro válido.")

def validar_status(s: str) -> bool:
    return s in ("pendente", "concluido")
