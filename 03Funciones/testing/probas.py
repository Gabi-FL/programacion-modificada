def encontrar_letra_dni(numero_dni: int) -> str:
    """te calcula la letra de tu dni

    Args:
        numero_dni (int): el dni sin letra

    Returns:
        str: la letra que te corresponde

    >>> encontrar_letra_dni(12345678)
    'Z'
    >>> encontrar_letra_dni(12345679)
    'S'
    >>> encontrar_letra_dni(0)
    'T'
    >>> encontrar_letra_dni (-123)
    'Número no válido'
    """
    letras = ["T", "R",	"W", "A", "G", "M",	"Y", "F", "P", "D", "X", "B", "N", "J", "Z", "S", "Q", "V", "H", "L", "C", "K", "E"]
    if numero_dni < 0 or numero_dni > 99999999:
        return "Número no válido"
    letra_dni = letras[numero_dni % 23]
    return letra_dni

numero_dni = int(input("Escribe el número de DNI sin letra"))
print(encontrar_letra_dni(numero_dni))