lista_opciones = ("carne", "verdura", "pescado", "marisco")
contador_elecciones = {"carne": 0, "verdura": 0, "pescado": 0, "marisco": 0}
lista_elecciones = []
respuesta = "s"

while respuesta == "s":
    print("Estas son las opciones:")
    for i in range(len(lista_opciones)):
        print(i + 1, lista_opciones[i])
    eleccion = int(input("Escoge una opción: "))
    lista_elecciones.append(lista_opciones[eleccion - 1])
    respuesta = input("¿Quieres añadir otro comensal? s/n: ")