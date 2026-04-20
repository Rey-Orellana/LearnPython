class Perro:
    def hablar(self):
        return "¡Guau!"

class Gato:
    def hablar(self):
        return "¡Miau!"

def hacer_ruido(animal):
    print(animal.hablar())

mascotas = [Perro(), Gato()]

for mascota in mascotas:
    hacer_ruido(mascota)