def mañana(hoy: str) -> str:
    """Recibe un día de la semana y devuelve el siguiente
        Args:
        hoy(str): el día como cadena de caracteres

    Returns:
        str: el día siguiente al que has escrito

    >>> mañana("lunes")
    'martes'
    >>> mañana("domingo")
    'lunes'
    >>> mañana("hola")
    'Valor no válido'
    """
    dias = ("lunes", "martes", "miércoles",
            "jueves", "viernes", "sábado", "domingo")
    if hoy in dias:
        return dias[(dias.index(hoy) + 1) % 7]
    else:
        return "Valor no válido"


hoy = input("escribe el nombre del día de la semana:\n")
print(mañana(hoy))
