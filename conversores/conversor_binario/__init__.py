def converterDecimalBinario(numero):

    numeroConvertido = ""

    numero = int(numero)

    while numero > 0:
        restoDivisao = numero % 2
        numero //= 2

        numeroConvertido += str(restoDivisao)

    numeroConvertido = numeroConvertido[::-1]

    return numeroConvertido

####################

def converterHexaBinario(numero):

    numeroConvertido = ""

    numeroHexaBinario = [['0', '0000'],['1', '0001'],['2', '0010'],['3', '0011'],['4', '0100'],['5', '0101'],['6', '0110'],['7', '0111'],['8', '1000'],['9', '1001'],['A', '1010'],['B', '1011'],['C', '1100'],['D', '1101'],['E', '1110'],['F', '1111']]

    numero = str.upper(numero)

    for algarismo in numero:
        for numeroBinario in numeroHexaBinario:
            if algarismo == numeroBinario[0]:
                numeroConvertido += numeroBinario[1]

    return numeroConvertido

####

def converterOctalBinario(numero):

    numeroConvertido = ""

    numerosOctalBinario = [['0', '000'],['1', '001'],['2', '010'],['3', '011'],['4', '100'],['5', '101'],['6', '110'],['7', '111']]

    for algarismo in numero:
        for numeroBinario in numerosOctalBinario:
            if algarismo == numeroBinario[0]:
                numeroConvertido += numeroBinario[1]

    return numeroConvertido