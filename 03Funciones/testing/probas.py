from datetime import date


def genera_identificador(nombre: str) -> str:
    """recibe el nombre de un usuario y le devuelve su identificador

    Args:
        nombre (str): el nombre completo del usuario

    Returns:
        str: el identificador de usuario
    >>> genera_identificador("Gabriel Fernández López")
    'a24gabrielfl'
    >>> genera_identificador("")
    'a24'
    >>> genera_identificador("Gabriel Fernandez")
    'a24gabrielf'
    >>> genera_identificador("Gabriel A")
    'a24gabriela'
    """
    tildes = "áéíóúüñç"
    equivalentes = "aeiouuñç"
    resultado = "a"
    hoy = date.today()
    anho = hoy.year
    anho_cadena = str(anho)
    resultado += anho_cadena[2:4]
    for elemento in nombre.split()[0]:
        resultado += elemento.lower()
    for elemento in nombre.split()[1:4]:
        resultado += elemento[0].lower()
    resultado_sin_tildes = ""
    for letra in resultado:
        if letra not in tildes:
            resultado_sin_tildes += letra
        else:
            indice = tildes.index(letra)
            resultado_sin_tildes += equivalentes[indice]
    return resultado_sin_tildes


nombre = input("Escribe el nombre completo del usuario: ")
print(genera_identificador(nombre))
