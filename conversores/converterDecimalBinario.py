def converterDecimalBinario(numero):

    numero_convertido = ""

    while numero > 0:
        resto_divisao = numero % 2
        numero //= 2

        numero_convertido += str(resto_divisao)

    numero_convertido = numero_convertido[::-1]

    return numero_convertido