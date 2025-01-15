class Circulo:
    radio: float
    centro: tuple[float, float]

    def __init__(self, radio: float, centro: tuple[float, float]):
        self.radio = radio
        self.centro = centro


c = Circulo(3, (0, 1))  # c es un objeto de tipo Circulo
print(c)
