class Libro:
    def __init__(self, titulo, autor):
        self.titulo = titulo
        self.autor = autor

    def __str__(self):
        return f"'{self.titulo}' escrito por {self.autor}"

mi_libro = Libro("El Quijote", "Cervantes")
print(mi_libro)  # Salida: 'El Quijote' escrito por Cervantes