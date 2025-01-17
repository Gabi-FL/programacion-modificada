class Punto:
    x: int
    y: int

    def __init__(self, x, y):
        self.x = x
        self.y = y
        if self.x > 100 or self.x < -100:
            self.x = 0
