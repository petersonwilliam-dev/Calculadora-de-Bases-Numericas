from validacao import validarNumero

from conversores.conversor_binario import converterOctalBinario, converterDecimalBinario, converterHexaBinario
from conversores.conversor_octal import converterBinarioOctal
from conversores.conversor_decimal import converterBinarioDecimal
from conversores.conversor_hexa import converterBinarioHexa


def converter(baseOriginal, baseConverter, numero):

    if not validarNumero(baseOriginal, numero):
        return "Número inválido"

    if baseOriginal == 10:
        numero = converterDecimalBinario(numero)
    elif baseOriginal == 8:
        numero = converterOctalBinario(numero)
    elif baseOriginal == 16:
        numero = converterHexaBinario(numero)


    if baseConverter == 10:
        numero = converterBinarioDecimal(numero)
    elif baseConverter == 8:
        numero = converterBinarioOctal(numero)
    elif baseConverter == 16:
        numero = converterBinarioHexa(numero)


    return numero