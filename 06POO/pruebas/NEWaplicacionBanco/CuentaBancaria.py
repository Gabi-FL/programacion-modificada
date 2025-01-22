class CuentaBancaria:
    nombre_titular: str
    numero_cuenta: str
    saldo: float

    def __init__(self, nombre_titular: str, numero_cuenta: str, saldo: float = 0):
        self.nombre_titular = nombre_titular
        self.numero_cuenta = numero_cuenta
        self.saldo = saldo

    def __str__(self):
        return (
            f"Titular: {self.nombre_titular}\n"
            f"Número de cuenta: {self.numero_cuenta}\n"
            f"Saldo: {self.saldo}\n"
        )

    def movimiento(self, cantidad: float, es_ingreso: bool = True):
        self.cantidad = cantidad
        self.es_ingreso = es_ingreso
        if es_ingreso:
            self.saldo += cantidad
        else:
            self.saldo -= cantidad
        return self.saldo >= 0
