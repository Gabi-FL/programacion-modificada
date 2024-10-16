limite = int(input(print("escribe el límite superior")))
contador = 0

for i in range (2, limite + 1):
    for j in range(i, 1, -1):
        if i % j != 0:
            contador += 1
print (contador)