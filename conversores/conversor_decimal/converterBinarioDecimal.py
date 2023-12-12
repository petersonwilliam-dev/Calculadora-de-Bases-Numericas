def converterBinarioDecimal(numero):

    numeroConvertido = 0
    numeroPotencia = 0

    numero = numero[::-1]

    for algarismo in numero:
        numeroConvertido += int(algarismo) * (2**numeroPotencia)

        numeroPotencia += 1

    return str(numeroConvertido)