class Persona:
    nombre: str
    edad: int
    dni: str

    def __init__(self, nombre: str, edad: int, dni: str):
        self.nombre = nombre
        self.edad = edad
        if Persona.comprobar_dni(dni):
            self.dni = dni
        else:
            raise AttributeError("DNI no válido")

    def __str__(self):
        return (f"Nombre: {self.nombre}\nEdad: {self.edad}\nDNI: {self.dni}")

    @staticmethod
    def comprobar_dni(dni):
        letras = ("T", "R",	"W", "A", "G", "M",	"Y", "F", "P", "D", "X", "B", "N", "J", "Z", "S", "Q", "V", "H", "L", "C", "K", "E")
        dni_sin_letra = int(dni[:8])
        return letras[dni_sin_letra % 23] == dni[-1]


if __name__ == "__main__":
    p1 = Persona("Manu", 21, "12345678B")
    print(Persona.comprobar_dni(p1.dni))
