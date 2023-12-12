from conversores.conversor_binario.converterHexaBinario import converterHexaBinario

def converterHexaDecimal(numero):

    numeroConvertido = 0
    expoente = 0

    numero = converterHexaBinario(numero)
    numero = numero[::-1]

    for algarismo in numero:

        numeroConvertido += int(algarismo) * (2**expoente)

        expoente += 1

    return str(numeroConvertido)
