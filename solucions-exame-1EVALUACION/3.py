def hai_12_uvas(lista: str) -> bool:
    """Determina se hai 12 uvas nunha lista.

    Args:
        lista (str): Lista coas uvas.

    Returns:
        bool: True se hai 12 uvas, False en caso contrario.
        
    >>> hai_12_uvas([['','o',''],['o','o','o'],['o','o','o']])
    False
    >>> hai_12_uvas([['o','o','','','',''],['o','o','','o'],['o','','','','o','o']])
    False
    >>> hai_12_uvas([['','o','','','',''],['o','o','','o'],['o','','','','o','o'],['o','','','o','o'], ['o','','','','o','o'], ['o','o']])
    False
    >>> hai_12_uvas([['','o','','','',''],['o','o','','o'],['o','','','','o','o'],['o','','','o','o'], ['o','','','','o',''], ['','']])
    True
    >>> hai_12_uvas([])
    False
    """
    contador = 0
    for fila in lista:
        for uva in fila:
            if uva == 'o':
                contador += 1
    if contador == 12:
        return True
    else:
        return False
    #return contador == 12

def determinar_posicion_uvas(lista: str) -> list[tuple[int, int]]:
    """Determina a posición das uvas nunha lista.

    Args:
        lista (str): Lista coas uvas.

    Returns:
        list[tuple[int, int]]: Lista coa posición das uvas.

    >>> determinar_posicion_uvas([['','o',''],['o','o','o'],['o','o','o']])
    [(0, 1), (1, 0), (1, 1), (1, 2), (2, 0), (2, 1), (2, 2)]
    >>> determinar_posicion_uvas([['o','o','','','',''],['o','o','','o'],['o','','','','o','o']])
    [(0, 0), (0, 1), (1, 0), (1, 1), (1, 3), (2, 0), (2, 4), (2, 5)]
    >>> determinar_posicion_uvas([['','o','','','',''],['o','o','','o'],['o','','','','o','o'],['o','','','o','o'], ['o','','','','o','o'], ['o','o']])
    [(0, 1), (1, 0), (1, 1), (1, 3), (2, 0), (2, 4), (2, 5), (3, 0), (3, 3), (3, 4), (4, 0), (4, 4), (4, 5), (5, 0), (5, 1)]
    >>> determinar_posicion_uvas([['','o','','','',''],['o','o','','o'],['o','','','','o','o'],['o','','','o','o'], ['o','','','','o',''], ['','']])
    [(0, 1), (1, 0), (1, 1), (1, 3), (2, 0), (2, 4), (2, 5), (3, 0), (3, 3), (3, 4), (4, 0), (4, 4)]
    >>> determinar_posicion_uvas([])
    []
    """
    lista_coordenadas = []
    for i in range(len(lista)):
        for j in range(len(lista[i])):
            if lista[i][j] == 'o':
                tupla = (i, j)
                lista_coordenadas.append(tupla)
    return lista_coordenadas


print(determinar_posicion_uvas([['','o','','','',''],['o','o','','o'],['o','','','','o','o'],['o','','','o','o'], ['o','','','','o',''], ['','']]))