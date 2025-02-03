class Punto:
    __x: int
    __y: int

    def __init__(self, x, y):
        self.x = x
        self.y = y
        if self.x > 100 or self.x < -100:
            self.x = 0
        if self.y > 100 or self.y < -100:
            self.y = 0

    @property
    def x(self):
        return self.__x

    @x.setter
    def x(self, x: int):
        if Punto.puntoXcorrecto(x):
            self.__x = x
        else:
            self.__x = x

    @staticmethod
    def puntoXcorrecto(x: int):
        if x > 100 or x < -100:
            return True
        else:
            return False

    @property
    def y(self):
        return self.__y

    @y.setter
    def y(self, y: int):
        if Punto.puntoYcorrecto(y):
            self.__y = y
        else:
            self.__y = y

    @staticmethod
    def puntoYcorrecto(y: int):
        if y > 100 or y < -100:
            return True
        else:
            return False

    def moverHorizontal(self, positivo: bool, valor: int):
        if positivo:
            self.x = (self.x + valor) % 100
        else:
            self.x = (self.x + valor) % 100

    def moverVertical(self, positivo: bool, valor: int):
        if positivo:
            self.y = (self.y + valor) % 100
        else:
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


class Linea:
    coordenadas: list[object]

    def __init__(self, p1, p2):
        self.p1 = [Punto.x, Punto.y]
        self.p2 = [Punto.x, Punto.y]
        self.coordenadas = [p1, p2]

    def moverHorizontal(self, positivo: bool, valor: int)-> bool:


    def moverVertical(self, positivo: bool, valor: int):
