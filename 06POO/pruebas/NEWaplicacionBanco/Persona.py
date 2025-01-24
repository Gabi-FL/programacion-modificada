class Persona:
    nombre: str
    __edad: int
    __dni: str

    def __init__(self, nombre: str, edad: int, dni: str):
        self.nombre = nombre
        self.dni = dni
        self.edad = edad

    def __str__(self):
        return (f"Nombre: {self.nombre}\nEdad: {self.edad}\nDNI: {self.dni}")

    @property
    def dni(self):
        return self.__dni

    @dni.setter
    def dni(self, dni):
        if (Persona.comprobar_dni(dni)):
            self.__dni = dni
        else:
            raise Exception("DNI incorrecto")

    @staticmethod
    def comprobar_dni(dni):
        letras = (
            "T", "R", "W", "A", "G", "M", "Y", "F", "P", "D", "X", "B", "N",
            "J", "Z", "S", "Q", "V", "H", "L", "C", "K", "E")
        if len(dni) == 9 and letras[int(dni[:8]) % 23] == dni[-1]:
            return True
        else:
            raise ValueError("DNI incorrecto")

    @property
    def edad(self):
        return self.__edad

    @edad.setter
    def edad(self, edad):
        if (Persona.comprobar_edad(edad)):
            self.__edad = edad
        else:
            raise ValueError("Edad incorrecta")

    @staticmethod
    def comprobar_edad(edad):
        if isinstance(edad, int) and (edad >= 0 and edad < 120):
            return True


if __name__ == "__main__":
    try:
        p1 = Persona("Pepe", 30, "12345678B")
        p2 = Persona("Manu", -21, "12345678Z")
        print(p1)
        print(p2)
    except Exception as e:
        print(e)
