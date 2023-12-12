def converterOctalBinario(numero):

    numeroConvertido = ""

    numerosOctalBinario = [['0', '000'],['1', '001'],['2', '010'],['3', '011'],['4', '100'],['5', '101'],['6', '110'],['7', '111']]

    for algarismo in numero:
        for numeroBinario in numerosOctalBinario:
            if algarismo == numeroBinario[0]:
                numeroConvertido += numeroBinario[1]

    return numeroConvertido