class Punto:
    x: int
    y: int

    def __init__(self, x, y):
        self.x = x
        self.y = y
        if self.x > 100 or self.x < -100:
            self.x = 0
        if self.y > 100 or self.y < -100:
            self.y = 0

    def moverHorizontal(self, positivo: bool, valor: int):
        if positivo:
            self.x = (self.x + valor) % 100
        if positivo is False:
            self.x = (self.x + valor) % 100

    def moverVertical(self, positivo: bool, valor: int):
        if positivo:
            self.y = (self.y + valor) % 100
        if positivo is False:
            self.y = (self.y + valor) % 100

    def obtenerCuadrante(self):
        if self.x > 0 and self.y > 0:
            return 1
        if self.x < 0 and self.y > 0:
            return 2
        if self.x < 0 and self.y < 0:
            return 3
        if self.x > 0 and self.y < 0:
            return 4

    def __str__(self):
        return f"[{self.x}, {self.y}]"
