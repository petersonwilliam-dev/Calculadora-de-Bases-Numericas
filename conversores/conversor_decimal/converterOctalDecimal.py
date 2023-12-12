from conversores.conversor_binario.converterOctalBinario import converterOctalBinario

def converterOctalDecimal(numero):

    numeroConvertido = 0
    expoente = 0

    numero = converterOctalBinario(numero)
    numero = numero[::-1]

    for algarismo in numero:
        numeroConvertido += int(algarismo) * (2**expoente)
        expoente += 1

    return str(numeroConvertido)
