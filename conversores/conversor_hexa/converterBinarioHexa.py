def converterBinarioHexa(numero):

    numerosBinarioHexa = [['0', '0000'],['1', '0001'],['2', '0010'],['3', '0011'],['4', '0100'],['5', '0101'],['6', '0110'],['7', '0111'],['8', '1000'],['9', '1001'],['A', '1010'],['B', '1011'],['C', '1100'],['D', '1101'],['E', '1110'],['F', '1111']]
    numeroConvertido = ""
    tamanhoNumero = len(numero)

    if (tamanhoNumero % 4 != 0):
        if tamanhoNumero % 4 == 3:
            numero = "000" + numero
        elif tamanhoNumero % 4 == 2:
            numero = "00" + numero
        else:
            numero = "0" + numero

    tamanhoIntervalo = 4

    for i in range(0, tamanhoNumero, tamanhoIntervalo):
        for numerosBinario in numerosBinarioHexa:
            if (numero[i:i+tamanhoIntervalo] == numerosBinario[1]):
                numeroConvertido += numerosBinario[0]

    return numeroConvertido