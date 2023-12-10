def converterOctalBinario(numero):

    numero_convertido = ""

    numeros_octal_binario = [['0', '000'],['1', '001'],['2', '010'],['3', '011'],['4', '100'],['5', '101'],['6', '110'],['7', '111']]

    numero = str(numero)

    for algarismo in numero:
        for numero_binario in numeros_octal_binario:
            if algarismo == numero_binario[0]:
                numero_convertido += numero_binario[1]

    return numero_convertido