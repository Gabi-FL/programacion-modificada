lista_opciones = ('carne', 'verdura', 'pescado', 'marisco')
lista_elecciones = []
respuesta = 's'


def contador(lista_elecciones: list) -> dict:
    """recibe una lista con las elecciones de los comensales y crea un
    diccionario con el número de cada tipo de elección

    Args:
        lista_elecciones (list): la lista con las elecciones

    Returns:
        dict: el diccionario con el recuento

    >>> contador(['carne', 'verdura', 'pescado', 'marisco'])
    {'carne': 1, 'verdura': 1, 'pescado': 1, 'marisco': 1}
    >>> contador(['carne', 'carne', 'carne', 'carne'])
    {'carne': 4, 'verdura': 0, 'pescado': 0, 'marisco': 0}
    >>> contador([])
    {'carne': 0, 'verdura': 0, 'pescado': 0, 'marisco': 0}
    """
    contador_elecciones = {
        'carne': 0,
        'verdura': 0,
        'pescado': 0,
        'marisco': 0
    }
    for elemento in lista_elecciones:
        if elemento == 'carne':
            contador_elecciones['carne'] += 1
        elif elemento == 'verdura':
            contador_elecciones['verdura'] += 1
        elif elemento == 'pescado':
            contador_elecciones['pescado'] += 1
        else:
            contador_elecciones['marisco'] += 1
    return contador_elecciones


while respuesta == 's':
    print('\nEstas son las opciones:')
    for i in range(len(lista_opciones)):
        print(i + 1, lista_opciones[i])
    eleccion = int(input('Escoge una opción: '))
    lista_elecciones.append(lista_opciones[eleccion - 1])
    respuesta = input('¿Quieres añadir otro comensal? s/n: ')

for clave in contador(lista_elecciones):
    print(clave, contador(lista_elecciones)[clave])
