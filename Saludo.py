class Personaje:
    def __init__(self, nombre, fuerza):
        self.nombre = nombre
        self.fuerza = fuerza

    def atacar(self, enemigo):
        print(f"{self.nombre} ataca a {enemigo} con {self.fuerza} de daño")

heroe = Personaje("Arturo", 50)
villano = Personaje("Dr. Mal", 30)

heroe.atacar(villano.nombre)