def celsius_a_fahrenheit(gradosC: float) -> float:
    '''
    Convierte grados Celsius a Fahrenheit

    Parámetros:
    gradosC (float): Los grados en Celsius

    Devuelve:
    float: Los grados covnertidos a Fahrenheit

    >>> celsius_a_fahrenheit(0)
    32.0
    >>> celsius_a_fahrenheit(100)
    212.0
    >>> celsius_a_fahrenheit(-40)
    -40.0
    >>> celsius_a_fahrenheit(37)
    98.6
    >>> celsius_a_fahrenheit(-10)
    14.0
    '''

    return (gradosC * 9 / 5) + 32