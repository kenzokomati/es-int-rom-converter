def int_to_roman(num):
    # Verificar se o número é válido
    if not isinstance(num, int):
        raise ValueError("A entrada deve ser um número inteiro.")
    if num <= 0:
        raise ValueError("A entrada deve ser um número positivo e maior que zero.")
    
    # Definir as combinações de números romanos
    val = [
        1000, 900, 500, 400,
        100, 90, 50, 40,
        10, 9, 5, 4,
        1
    ]
    syb = [
        "M", "CM", "D", "CD",
        "C", "XC", "L", "XL",
        "X", "IX", "V", "IV",
        "I"
    ]

    roman_numeral = ''

    # Para cada valor, dividir o número
    for i in range(len(val)):
        while num >= val[i]:
            roman_numeral += syb[i]
            num -= val[i]

    return roman_numeral
