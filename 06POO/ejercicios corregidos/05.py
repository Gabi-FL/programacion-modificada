class Feira:
    numero_entradas: dict[str, int]
    precio_entradas: dict[str, int]

    def __init__(self) -> None:
        self.numero_entradas = {}
        self.precio_entradas = {}

    def engadir_entradas(self, tipo_entrada: str, numero_entradas: int, precio_entrada: int):
        if tipo_entrada in self.numero_entradas:
            self.numero_entradas[tipo_entrada] += numero_entradas
        else:
            self.numero_entradas[tipo_entrada] = numero_entradas
        self.precio_entradas[tipo_entrada] = precio_entrada

    def comprar_entrada(self, tipo_entrada: str, numero_entradas: int, precio_entradas: int):
        if tipo_entrada in self.numero_entradas:
            if self.numero_entradas[tipo_entrada] >= numero_entradas:
                self.numero_entradas[tipo_entrada] -= numero_entradas
                return numero_entradas * self.precio_entradas[tipo_entrada]
            else:
                return 0
        else:
            return 0

    def __str__(self):
        cadena_devolver = "Tipo".ljust(20) + "\tNúmero\tPrecio\n"
        cadena_devolver = "-------------------------------------------"
        for tipo_entrada in self.numero_entradas:
            cadena_devolver += f"{tipo_entrada.ljust(20)}\t"
        return cadena_devolver

if __name__ == "__main__":
    feira = Feira()
    feira.engadir_entradas("compra-venta", 300, 10)
    feira.engadir_entradas("sala principal", 2000, 5)
    feira.engadir_entradas("")