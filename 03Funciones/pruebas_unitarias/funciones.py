def es_bisiesto(anho: int) -> bool:
    '''
    Recibe un año y determina si es bisiesto o no.
    
    Parámetros
    ----------
    anho: int
        Año a evaluar.
        
    Devuelve
    -------
    bool
        True si el año es bisiesto, False en caso contrario.

>>> es_bisiesto(2000)
True
>>> es_bisiesto(1900)
False
>>> es_bisiesto(1996)
True
>>> es_bisiesto(1997)
False
    '''

    
    if (anho % 4 == 0 and anho % 100 != 0) or anho % 400 == 0:
        return True
    return False