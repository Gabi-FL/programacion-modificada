
n_bloques = int(input("Escribe el número de bloques que hay disponibles:\n"))
altura = 0
while n_bloques >= (altura + 1):
    altura += 1
    n_bloques -= altura
print (altura)