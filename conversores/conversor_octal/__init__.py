def converterBinarioOctal(numero):

    numerosOctalBinario = [['0', '000'], ['1', '001'], ['2', '010'], ['3', '011'], ['4', '100'], ['5', '101'], ['6', '110'], ['7', '111']]

    numeroConvertido = ""
    tamanhoNumeroBinario = len(numero)

    if ((tamanhoNumeroBinario % 3) != 0):
        if (tamanhoNumeroBinario % 3 == 1):
            numero = "00" + numero
        else:
            numero = "0" + numero

    tamanhoIntervalo = 3

    for i in range(0, tamanhoNumeroBinario, tamanhoIntervalo):
        for numerosBinario in numerosOctalBinario:
            if (numero[i:i + tamanhoIntervalo] == numerosBinario[1]):
                numeroConvertido += numerosBinario[0]

    return numeroConvertido