class CuentaBancaria:
    nombre_titular: str
    numero_cuenta: str
    saldo: float

    def __init__(self, nombre_titular: str, numero_cuenta: str, saldo: float=0):
        self.nombre_titular = nombre_titular
        self.numero_cuenta = numero_cuenta
        self.saldo = saldo

    def __str__(self):
        