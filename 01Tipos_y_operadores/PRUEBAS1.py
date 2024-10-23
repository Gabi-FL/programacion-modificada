
import math

def area_cir(radio):
    return radio ** 2 * math.pi

r = "s"
suma = 0

while r == "s":
    cantidad = int(input("¿cuántos posavasos quieres? "))
    radio = int(input("Escribe el radio del posavasos "))
    area = area_cir(radio) * cantidad
    suma += area
    r = input("¿quieres añadir más a tu pedido? s/n ")

print(f"En total necesitarás {suma}")