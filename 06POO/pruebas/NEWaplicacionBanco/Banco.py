from CuentaBancaria import CuentaBancaria
from Persona import Persona

class Banco:
    nome: str
    enderezo: str
    telefono: str
    contas_bancarias: list[CuentaBancaria]

    def __init__(self, nome: str, enderezo: str, telefono: str):
        self.nome = nome
        self.enderezo = enderezo
        self.telefono = telefono
        self.contas_bancarias = []

    def agregar_conta(self, conta: CuentaBancaria):
        self.contas_bancarias.append(conta)

    def __str__(self):
        resultado = f"Banco: {self.nome}, {self.enderezo}, {self.telefono}, con contas:\n"
        for conta in self.contas_bancarias:
            resultado += str(conta) + "\n"
        return resultado


if __name__ == "__main__":
    b = Banco("Abanca", "Teis", "986789456")
    p = Persona("Ana González", 31, "12345678Z")
    c = CuentaBancaria(p, "7894561337")
    b.agregar_conta(c)
    print(b)
