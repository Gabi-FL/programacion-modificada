def comp_pal_frase(frase: str) -> bool:
    """comprueba si una frase es un palíndromo

    Args:
        frase (str): la frase que el usuario escribe

    Returns:
        bool: booleano de si es palindromo o no

    >>> comp_pal_frase("La ruta nos aporto otro paso natural")
    True
    >>> comp_pal_frase("Ana come pan")
    """
    frase_min = frase.lower()
    lista_solo_letras = ""
    for letra in frase_min:
        if letra.isalpha:
            lista_solo_letras += letra
    if lista_solo_letras == lista_solo_letras[::-1]:
        return True
    else:
        return False


print(comp_pal_frase("La ruta nos aporto otro paso natural"))