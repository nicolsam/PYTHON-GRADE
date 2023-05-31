def TransformarEmMaiusculo(array: list[str]):
    maiusculo = list(map(lambda texto: str.upper(texto), array))
    return maiusculo