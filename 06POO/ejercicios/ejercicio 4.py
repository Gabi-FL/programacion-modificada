class Alumnx:
    nombreCompleto: str
    dni: str
    edad: int
    escuela: str

    def __init__(self, nombreCompleto, dni, edad, escuela) -> None:
        self.nombreCompleto = nombreCompleto
        self.dni = dni
        self.edad = edad
        self.escuela = escuela

    def mayor_o_no(self) -> bool:
        if self.edad >= 18:
            return True
        return False

    def __ge__(self, other) -> bool:
        return self.edad >= other.edad

    def __gt__(self, other) -> bool:
        return self.edad > other.edad

    def __le__(self, other) -> bool:
        return self.edad <= other.edad

    def __lt__(self, other) -> bool:
        return self.edad < other.edad

    def __eq__(self, other) -> bool:
        return self.dni == other.dni


a1 = Alumnx("Manu Tenorio", "12365487V", 21, "Del Avida")
a2 = Alumnx("Rubén Tosa", "12345678M", 17, "Machachuches")

print(a1.mayor_o_no())
print(a2.mayor_o_no())
print(a1 >= a2)
print(a1 > a2)
print(a1 <= a2)
print(a1 < a2)
print(a1 == a2)
