from CuentaBancaria import CuentaBancaria
from Persona import Persona


p1 = Persona("Manu Tenorio", 21, "12345678Z")
print(p1)
c1 = CuentaBancaria(p1, "1234567890")
print(c1)
c1.movimiento(1000, True)
print(c1)
c1.movimiento(200, False)
print(c1)
