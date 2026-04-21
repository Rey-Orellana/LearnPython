class Celular:
    def __init__(self, marca):
        self.marca = marca

    def llamar(self):
        print(f"Llamando desde mi {self.marca}...")

mi_cel = Celular("iPhone")
mi_cel.llamar()