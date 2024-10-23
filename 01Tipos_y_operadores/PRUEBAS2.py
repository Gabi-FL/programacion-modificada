def es_bisiesto(año):
    if (año % 4 != 0):
        return False
    elif (año % 100 != 0):
        return True
    elif (año % 400 != 0):
        return False
    else:
        return True
    
min = int(input("escribe el año de inicio "))
max = int(input("Escribe el año final "))

for i in range(min, max + 1):
    print(i, "es bisiesto" if es_bisiesto(i) else "no es bisiesto")