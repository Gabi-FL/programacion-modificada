class Linea:
    coordenadas: list[object]

    def __init__(self, p1, p2):
        if p1.x > 100 or p1.x < -100:
            p1.x = 0
        if p1.y > 100 or p1.y < -100:
            p1.y = 0
        if p2.x > 100 or p2.x < -100:
            p2.x = 0
        if p2.y > 100 or p2.y < -100:
            p2.y = 0
        return self.coordenadas

    def moverHorizontal(self, positivo: bool, valor: int)-> bool:
        if positivo:
            self.coordenadas = (self.coordenadas + valor)
        if positivo is False:
            self.coordenadas = (self.coordenadas + valor)

    def moverVertical(self, positivo: bool, valor: int):
        
        if positivo:
            self.coordenadas = (self.coordenadas + valor)
        if positivo is False:
            self.coordenadas = (self.coordenadas + valor)
