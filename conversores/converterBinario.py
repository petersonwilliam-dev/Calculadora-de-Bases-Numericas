def converterBinario(numero, baseInicial):

    numeroConvertido = ""

    if baseInicial == 10:
        while numero > 0:
            restoDivisao = numero % 2
            numero //= 2

            numeroConvertido += str(restoDivisao)

    return numeroConvertido[::-1]