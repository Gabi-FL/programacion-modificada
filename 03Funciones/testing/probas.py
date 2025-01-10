lista_nombres = ["Pedro", "Manu", "Rubén", "Pablo", "Rubén"]
contador = 0
inicio = 0
hay_mas = True
try:
    nombre = input("Introduce un nombre")
    while hay_mas:
        try:
            for elemento in lista_nombres:
                nombre_encontrado = lista_nombres.index(nombre, inicio)
                inicio = nombre_encontrado + 1
                contador += 1
        except ValueError:
            print(f"{nombre} aparece {contador}", "vez" if contador == 1 else "veces", "en la lista")
            hay_mas = False
except:
    print("Ha ocurrido un error")
