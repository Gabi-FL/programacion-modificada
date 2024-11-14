def encontrar_letra_dni(numero_dni: int) -> str:
    letras = ["T", "R",	"W", "A", "G", "M",	"Y", "F", "P", "D", "X", "B", "N", "J", "Z", "S", "Q", "V", "H", "L", "C", "K", "E"]
    letra_dni = letras[numero_dni - ((numero_dni // 23) * 23)]
    return letra_dni

numero_dni = 39455246
print(encontrar_letra_dni(numero_dni))