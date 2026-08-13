def calcular_total(itens, desconto_percentual=0, cupom=None):
    """
    Calcula o total de uma compra.

    Cada item representa uma tupla no formato:
    (preco_unitario, quantidade)
    """
    if not 0 <= desconto_percentual <= 100:
        raise ValueError("O desconto precisa estar entre 0 e 100.")

    # Regra do Cupom de Desconto
    desconto_cupom = 0
    if cupom is not None:
        cupom_limpo = cupom.strip().upper()
        if cupom_limpo == "DEVOPS10":
            desconto_cupom = 10
        else:
            raise ValueError("Cupom inválido")

    subtotal = sum(
        preco_unitario * quantidade
        for preco_unitario, quantidade in itens
    )

    # Soma o desconto percentual normal + o desconto do cupom
    desconto_total = desconto_percentual + desconto_cupom

    total = subtotal - ((subtotal / 100) * desconto_total)

    return round(total, 2)
