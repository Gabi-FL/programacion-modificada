class Libro:
    titulo: str
    autor: str
    ejemplaresTotales: int
    ejemplaresPrestados: int

    def __init__(self, titulo: str, autor: str, ejemplaresTotales: int):
        self.titulo = titulo
        self.autor = autor
        self.ejemplaresTotales = ejemplaresTotales
        self.ejemplaresPrestados = 0

    def __str__(self) -> str:
        return (
            f"Libro:\n\tTítulo: {self.titulo}\n\tAutor: {self.autor}\n\t"
            f"Ejemplares disponibles: {self.ejemplaresTotales - self.ejemplaresPrestados}/{self.ejemplaresTotales}"
        )

    def prestar(self) -> bool:
        if self.ejemplaresTotales > self.ejemplaresPrestados:
            self.ejemplaresPrestados += 1
            return True
        return False

    def devolver(self) -> bool:
        if self.ejemplaresPrestados > 0:
            self.ejemplaresPrestados -= 1
            return True
        return False


if __name__ == "__main__":
    l1 = Libro("Harry Potter", "J.K. Rowling", 5)

    print(l1)
    print(l1.prestar())
    print(l1)
    print(l1.devolver())
    print(l1)
