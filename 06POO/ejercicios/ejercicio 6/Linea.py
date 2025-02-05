from Punto import Punto


class Linea:
    __coordenadas: list[Punto]

    def __init__(self, p1: Punto, p2: Punto):
        self.__coordenadas = [p1, p2]

    def __str__(self):
        return f"Liña que pasa por {self.__coordenadas[0]} e {self.__coordenadas[1]}"

    def moverHorizontal(self, positivo: bool, valor: int):
        self.__coordenadas[0].moverHorizontal(positivo, valor)
        self.__coordenadas[1].moverHorizontal(positivo, valor)

    def moverVertical(self, positivo: bool, valor: int):
        self.__coordenadas[0].moverVertical(positivo, valor)
        self.__coordenadas[1].moverVertical(positivo, valor)


if __name__ == "__main__":
    p1 = Punto(2, 1)
    p2 = Punto(-3, -4)
    linea = Linea(p1, p2)
    print(linea)
    linea.moverHorizontal(True, 10)
    print(linea)
    linea.moverVertical(True, 10)
    print(linea)
