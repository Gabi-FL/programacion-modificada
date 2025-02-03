class Alumnx:
    nombreCompleto: str
    __dni: str
    __edad: int
    escuela: str

    def __init__(self, nombreCompleto, dni, edad, escuela) -> None:
        self.nombreCompleto = nombreCompleto
        self.dni = dni
        self.edad = edad
        self.escuela = escuela

    @property
    def dni(self):
        return self.__dni

    @dni.setter
    def dni(self, dni: str):
        if Alumnx.dni_correcto(dni):
            self.__dni = dni
        else:
            raise Exception("DNI incorrecto")

    @property
    def edad(self):
        return self.__edad

    @edad.setter
    def edad(self, edad):
        if edad >= 0:
            self.__edad = edad
        else:
            raise Exception("La edad no puede ser negativa")

    @staticmethod
    def dni_correcto(dni: str) -> bool:
        letras = "TRWAGMYFPDXBNJZSQVHLCKE"
        if len(dni) != 9:
            return False
        if not dni[-1].isalpha():
            return False
        if not dni[:8].isdigit():
            return False
        resto = int(dni[:8]) % 23
        if dni[-1].upper() != letras[resto]:
            return False
        return True

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

    def __str__(self):
        return (f"{self.nombreCompleto} ({self.dni}) y edad {self.edad}, estudiante de {self.escuela}")


if __name__ == "__main__":
    try:
        a1 = Alumnx("Manu Tenorio", "12345678Z", 21, "Del Avida")
        a2 = Alumnx("Rubén Tosa", "12345678Z", 17, "Machachuches")
        print(a1.dni)
        print(a1.mayor_o_no())
    except Exception as e:
        print(e)
    print(a1.mayor_o_no())
    print(a2.mayor_o_no())
    print(a1 >= a2)
    print(a1 > a2)
# print(a1 <= a2)
# print(a1 < a2)
# print(a1 == a2)
