import time


class Luz:
    color: tuple
    valor: int

    def __init__(self):
        self.color = ("verde", "ámbar", "rojo")
        self.valor = 1

    def cambia_color(self):
        self.valor = (self.valor + 1) % len(self.color)
        return self.color[self.valor]
