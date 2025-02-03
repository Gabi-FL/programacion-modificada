class Linea:
    coordenadas: list

    def __init__(self, x, y):
        self.coordenadas = [x, y]
        if self.x > 100 or self.x < -100:
            self.x = 0
        if self.y > 100 or self.y < -100:
            self.y = 0
        return self.coordenadas

    def moverHorizontal(self, positivo: bool, valor: int):
        if positivo:
            self.coordenadas = (self.coordenadas + valor)
        if positivo is False:
            self.coordenadas = (self.coordenadas + valor)

    def moverVertical(self, positivo: bool, valor: int):
        if positivo:
            self.coordenadas = (self.coordenadas + valor)
        if positivo is False:
            self.coordenadas = (self.coordenadas + valor)
