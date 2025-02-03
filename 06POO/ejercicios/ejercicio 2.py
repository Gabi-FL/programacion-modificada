class Rectangulo:
    base: int
    altura: int

    def __init__(self, base: int = 0, altura: int = 0):
        self.base = base
        self.altura = altura

    def area(self) -> float:
        return self.base * self.altura

    def __str__(self) -> str:
        return (
            f"El área del rectángulo es {self.area()}"
            f"y su altura es {self.altura}"
        )

    def es_cuadrado(self) -> bool:
        if self.base == self.altura and self.base != 0:
            return True
        return False


if __name__ == "__main__":
    rect1 = Rectangulo(2, 3)
    print(rect1.area())
    print(rect1)
    print("Es un cuadrado" if rect1.es_cuadrado() else "No es un cuadrado")
