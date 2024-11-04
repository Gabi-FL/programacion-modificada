def es_mayor_edad(edad: int) -> bool: 
    '''
    Permite comprobar si una persona es mayor de edad o no.

    Parámetros:
    edad: int
        La edad de la persona.
    
    Devuelve:
    bool
        True si es mayor de edad y False en caso contrario

    >>> es_mayor_edad(15)
    False
    >>> es_mayor_edad(20)
    True
    >>> es_mayor_edad(18)
    True
    '''
    if edad >= 18:
        return True
    else:
        return False