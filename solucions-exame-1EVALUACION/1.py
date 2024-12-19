def determinar_maioría(opcions: tuple[str], escollas: list[str]) -> str:
    """
    Determina a opción máis escollida dunha lista de escollas.
    
    Args:
        opcions (list[str]): Lista de opcións posibles.
        escollas (list[str]): Lista de escollas realizadas.
        
    Returns:
        str: A opción máis escollida.
        
    >>> determinar_maioría(("marisco", "carne", "pescado", "pavo", "verdura"), ["marisco", "carne", "pescado", "pavo", "verdura", "marisco", "carne", "pescado", "pavo", "verdura", "marisco", "carne", "pescado", "pavo", "verdura", "marisco", "carne", "pescado", "pavo", "verdura", "marisco", "carne", "pescado", "pavo", "verdura", "marisco", "carne", "pescado", "pavo", "verdura", "marisco", "carne", "pescado", "pavo", "verdura", "marisco", "carne", "pescado", "pavo", "verdura", "marisco", "carne", "pescado", "pavo", "verdura"])
    'marisco'
    >>> determinar_maioría(("marisco", "carne", "pescado", "pavo", "verdura"), ["marisco", "carne", "carne", "pescado"])
    'carne'
    >>> determinar_maioría(("marisco", "carne", "pescado", "pavo", "verdura"), ["marisco", "carne", "pescado"])
    'marisco'
    """
    ganadora = opcions[0]
    for opcion in opcions:
        if escollas.count(opcion) > escollas.count(ganadora):
            ganadora = opcion
    return ganadora

    # contador = [0 for i in range(len(opcions))]
    # for escolla in escollas:
    #     posicion = opcions.index(escolla)
    #     contador[posicion] += 1
    # return opcions[contador.index(max(contador))]
    #
    # contador = []
    # for escolla in escollas:
    #     contador.append(escollas.count(escolla))
    # mas_popular = contador.index(max(contador))
    # return escollas[mas_popular]

determinar_maioría(("marisco", "carne", "pescado", "pavo", "verdura"), ["marisco", "carne", "carne", "pescado"])

opcions = ("marisco", "carne", "pescado", "pavo", "verdura")

escollas = []
resposta = "s"
while resposta == "s":
    print("Benvido á aplicación para seleccionar a cea de fin de ano, faga a súa escolla:")
    for i in range(len(opcions)):
        print(i, ". ", opcions[i], sep="")
    valor = int(input("Escolla unha opción: "))
    escollas.append(opcions[valor])
    resposta = input("Quere seguir escollendo? (s/n): ")
print(escollas)