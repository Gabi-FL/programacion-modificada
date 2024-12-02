def num_palabras(frase: str) -> int:
    """recibe una frase y te cuenta las palabras

    Args:
        frase (str): la frase

    Returns:
        int: el número de palabras
    >>> num_palabras("Hola")
    1
    >>> num_palabras("Hola mundo")
    2
    >>> num_palabras("Hola mundo cruel")
    3
    >>> num_palabras("")
    0
    """
    contador = len(frase.split())
    return contador


frase = input("escribe una frase: ")
print(num_palabras(frase))
