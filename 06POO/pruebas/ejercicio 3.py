import time


class Luz:
    color: tuple
    valor: int

    def __init__(self):
        self.color = ("verde", "ámbar", "rojo")
        self.valor = 1

    def cambia_color(self):
        self.valor += 1
        if self.valor > 2:
            self.valor = 0
        return self.color[self.valor]


contador = 0
semaforo = Luz()
while contador < 6:
    print(semaforo.cambia_color())
    contador += 1
    time.sleep(2)
    print(semaforo.cambia_color())
    contador += 1
    time.sleep(2)
    print(semaforo.cambia_color())
    contador += 1
    time.sleep(2)
