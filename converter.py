from conversores.conversor_binario.converterOctalBinario import converterOctalBinario
from conversores.conversor_binario.converterHexaBinario import converterHexaBinario
from conversores.conversor_binario.converterDecimalBinario import converterDecimalBinario
from conversores.conversor_decimal.converterBinarioDecimal import converterBinarioDecimal
from conversores.conversor_octal.converterBinarioOctal import converterBinarioOctal
from conversores.conversor_hexa.converterBinarioHexa import converterBinarioHexa

def converter(baseOriginal, baseConverter, numero):

    numeroConvertido = ""

    caracteresHexa = ['0','1','2','3','4','5','6','7','8','9','A','B','C','D','E','F']

    if (baseOriginal != 16):
        if not (numero.isnumeric()):
            return "Número inválido"

        else:
            for algarismo in numero:
                if (int(algarismo) >= baseOriginal):
                    return "Número inválido"

    else:
        for algarismo in numero:
            if not algarismo in caracteresHexa:
                return "Número inválido"

    if baseConverter == 10:
        if baseOriginal == 2:
            numeroConvertido = converterBinarioDecimal(numero)
        elif baseOriginal == 8:
            numeroConvertido = converterBinarioDecimal(converterOctalBinario(numero))
        elif baseOriginal == 16:
            numeroConvertido = converterBinarioDecimal(converterHexaBinario(numero))

    elif baseConverter == 8:
        if baseOriginal == 2:
            numeroConvertido = converterBinarioOctal(numero)
        elif baseOriginal == 10:
            numeroConvertido = converterBinarioOctal(converterDecimalBinario(numero))
        elif baseOriginal == 16:
            numeroConvertido = converterBinarioOctal(converterHexaBinario(numero))

    elif baseConverter == 16:
        if baseOriginal == 2:
            numeroConvertido = converterBinarioHexa(numero)
        elif baseOriginal == 8:
            numeroConvertido = converterBinarioHexa(converterOctalBinario(numero))
        elif baseOriginal == 10:
            numeroConvertido = converterBinarioHexa(converterDecimalBinario(numero))

    elif baseConverter == 2:
        if baseOriginal == 10:
            numeroConvertido = converterDecimalBinario(numero)
        elif baseOriginal == 8:
            numeroConvertido = converterOctalBinario(numero)
        elif baseOriginal == 16:
            numeroConvertido = converterHexaBinario(numero)

    return numeroConvertido
