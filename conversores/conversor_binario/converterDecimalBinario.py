def converterDecimalBinario(numero):

    numeroConvertido = ""

    numero = int(numero)

    while numero > 0:
        restoDivisao = numero % 2
        numero //= 2

        numeroConvertido += str(restoDivisao)

    numeroConvertido = numeroConvertido[::-1]

    return numeroConvertido