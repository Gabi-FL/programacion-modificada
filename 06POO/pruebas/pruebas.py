class Libro:
    titulo: str
    autor: str
    EjemplaresTotales: int
    EjemplaresPrestados: int

    def __init__(self, titulo: str, autor: str, EjemplaresTotales: int, EjemplaresPrestados: int):
        self.titulo = titulo
        self.autor = autor
        self.EjemplaresTotales = EjemplaresTotales
        self.EjemplaresPrestados = EjemplaresPrestados

    def prestar(self) -> bool:
        if self.EjemplaresTotales > self.EjemplaresPrestados:
            self.EjemplaresPrestados += 1
            return True
        else:
            return False

    def devolver(self) -> bool:
        if self.EjemplaresPrestados > 0:
            self.EjemplaresPrestados -= 1
            return True
        else:
            return False


if __name__ == "__main__":
    l1 = Libro("Harry Potter", "J.K. Rowling", 5, 0)
    print(l1.prestar())
    print(l1.devolver())
