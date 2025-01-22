from CuentaBancaria import CuentaBancaria
from Persona import Persona


p1 = Persona("Manu Tenorio", 21, "12345678B")
#print(Persona.comprobar_dni(p1.dni))
print(p1)
c1 = CuentaBancaria(p1.nombre, "1234567890")
print(c1)
c1.movimiento(1000, True)
print(c1)
c1.movimiento(200, False)
print(c1)
