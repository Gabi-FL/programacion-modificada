lista = [24, 26, 27, 25, 21, 18, 15]
posicion1 = int(input("Escribe la primera posición: "))
posicion2 = int(input("Introduce la segunda posición: "))

try:
    print(f"La media es de {round((lista[posicion1 - 1] + lista[posicion2 - 1]) / 2, 2)}")
except IndexError:
    print("La media es 0")
except:
    print("Los valores introducidos no son válidos")