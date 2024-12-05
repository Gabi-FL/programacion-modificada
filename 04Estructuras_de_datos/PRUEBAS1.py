def penultima_vocal(verso: str) -> int:
    """Recibe un verso y busca la penúltima vocal

    Args:
        verso (str): el verso a analizar

    Returns:
        int: la posición de la penúltima vocal
    >>> penultima_vocal(casa)
    1
    >>> penultima_vocal(llanas)
    2
    >>> penultima_vocal(camino)
    3
    """
    vocales = "aeiouáéíóú"
    posicion = -1
    contador_vocales = 0
    for i in range(len(verso) -1, -1, -1):
        if verso[i] in vocales and contador_vocales < 2:
            contador_vocales += 1
            if contador_vocales == 2:
                posicion = i
    return posicion


def riman(verso1: str, verso2: str) -> bool:
    """determina si dos versos acabados en palabras graves tienen rima consonante

    Args:
        verso1 (str): el primer verso
        verso2 (str): el verso a comparar

    Returns:
        bool: si sí o si no
    >>> riman("casa", "pasa")
    True
    >>> riman("cuidado con la cosa", "o acabarás en la fosa")
    True
    >>> riman("vete al río", "que esto es mío")
    True
    >>> riman("vete a casa", "o te llevas una ostia")
    False
    """
    posicion_vocal1 = penultima_vocal(verso1)
    posicion_vocal2 = penultima_vocal(verso2)
    return verso1[posicion_vocal1:] == verso2[posicion_vocal2:]


print(riman("caca", "vaca"))