from CuentaBancaria import CuentaBancaria
from Persona import Persona
from Banco import Banco
from Vista import Vista

vista = Vista()
b = Banco("Abanca", "Teis", "986789456")
p1 = Persona("Manu Tenorio", 21, "12345678Z")
opcion = int(input(vista.menu1()))
if opcion == 1:
    CuentaBancaria(p1, "123456789123")




print(p1)
c1 = CuentaBancaria(p1, "1234567890")
print(c1)
c1.movimiento(1000, True)
print(c1)
c1.movimiento(200, False)
print(c1)
