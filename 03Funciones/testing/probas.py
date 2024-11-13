def crea_lista(posiciones: int) -> list:

    lista = []
    for i in range (posiciones):
        lista.append(int(input("Escribe un número: ")))
    print(lista)
    return lista

def invierte_lista(lista: list) -> list:
    """Invierte el orden de los elementos de una lista dada

    Args:
        lista (list): la lista que se le da

    Returns:
        list: la lsta con los elementos invertidos

    >>> invierte_lista([1, 2, 3, 4, 5])
    [5, 4, 3, 2, 1]
    >>> invierte_lista([])
    []
    >>> invierte_lista(['a', 'b', 'c'])
    ['c', 'b', 'a']
    """
    return lista[::-1]

lista = crea_lista(5)

lista_invertida = invierte_lista(lista)

print (lista_invertida)