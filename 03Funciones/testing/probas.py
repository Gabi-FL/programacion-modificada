def detecta_verbos(cadena: str) -> bool | None:
    """Recibe una palavbra y te dice si es un verbo o no

    Args:
        cadena (str): la palabra

    Returns:
        bool: devuelve verdadero o falso si es verbo o no

    >>> 'comer'
    True
    >>> 'vivir'
    True
    >>> 'hablar'
    True
    >>> 'programación'
    False
    """
    if cadena.endswith("ar") or cadena.endswith("er") or cadena.endswith("ir"):
        return True
    

cadena = input("Escribe la palabra: ")
print(f"la palabra {cadena} {"es un verbo" if detecta_verbos(cadena) else "no es un verbo"}")