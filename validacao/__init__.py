def validarNumero(base, numero):

    caracteresHexa = ['0','1','2','3','4','5','6','7','8','9','A','B','C','D','E','F']

    if base != 16:
        for algarismo in numero:
            if int(algarismo) >= base:
                return False
    else:
        for algarismo in numero:
            if not algarismo in caracteresHexa:
                return False

    return True

