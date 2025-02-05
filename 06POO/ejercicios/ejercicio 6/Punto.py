class Punto:
    __x: int
    __y: int

    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    @property
    def x(self):
        return self.__x

    @x.setter
    def x(self, x: int):
        if x <= 100 or x >= -100:
            self.__x = x
        else:
            self.__x = 0

    @property
    def y(self):
        return self.__y

    @y.setter
    def y(self, y: int):
        if y <= 100 or y >= -100:
            self.__y = y
        else:
            self.__y = 0

    def moverHorizontal(self, positivo: bool, valor: int):
        if positivo:
            self.x = min(self.x + valor, 100)
        else:
            self.x = max(self.x - valor, -100)

    def moverVertical(self, positivo: bool, valor: int):
        if positivo:
            self.y = min(self.y + valor, 100)
        else:
            self.y = max(self.y - valor, -100)

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


class Linea:
    coordenadas: list[object]

    def __init__(self, p1, p2):
        self.p1 = [Punto.x, Punto.y]
        self.p2 = [Punto.x, Punto.y]
        self.coordenadas = [p1, p2]

    def moverHorizontal(self, positivo: bool, valor: int)-> bool:
        pass

    def moverVertical(self, positivo: bool, valor: int):
        pass


if __name__ == "__main__":
    punto0 = Punto()
    print(punto0)
    punto1 = Punto(150, 200)
    print(punto1)
    punto = Punto(90, 60)
    punto.moverHorizontal(True, 5)
    print(punto)
    punto.moverHorizontal(False, 5)
    print(punto)
    punto.moverHorizontal(True, 20)
    print(punto)
    punto.moverHorizontal(False, 2000)
    print(punto)
