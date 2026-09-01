def binario_a_hexadecimal(binario):
    """
    Convierte una cadena binaria de 64 bits
    a un hexadecimal de 16 caracteres.
    """
    numero = int(binario, 2)
    return format(numero, "016X")


def hexadecimal_a_binario(hexadecimal):
    """
    Convierte un número hexadecimal
    a una cadena binaria de exactamente 64 bits.
    """
    numero = int(hexadecimal, 16)
    return format(numero, "064b")


def hexadecimal_valido(hexadecimal):
    """
    Verifica que el valor tenga entre 1 y 16 caracteres
    y que todos sean caracteres hexadecimales válidos.
    """

    if len(hexadecimal) == 0:
        return False

    if len(hexadecimal) > 16:
        return False

    caracteres_validos = "0123456789ABCDEF"

    for caracter in hexadecimal.upper():

        if caracter not in caracteres_validos:
            return False

    return True