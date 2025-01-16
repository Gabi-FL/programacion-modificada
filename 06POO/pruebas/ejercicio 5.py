class Feria:
    disponibles_ppal: int
    disponibles_comven: int
    disponibles_vip: int
    vendidas_ppal: int
    vendidas_comven: int
    vendidas_vip: int

    def __innit__(self):
        self.disponibles_ppal = 2000
        self.disponibles_comven = 300
        self.disponibles_vip = 20
        self.vendidas_ppal = 0
        self.vendidas_comven = 0
        self.vendidas_vip = 0

    def e_ppal(self):
        if self.disponibles_ppal > 0:
            self.disponibles_ppal -= 1
            self.vendidas_ppal += 1
            return True
        return False

    def e_comven(self):
        if self.disponibles_comven > 0:
            self.disponibles_comven -= 1
            self.vendidas_ppal += 1
            return True
        return False

    def e_vip(self):
        if self.disponibles_vip > 0:
            self.disponibles_vip -= 1
            self.vendidas_vip += 1
            return True
        return False
