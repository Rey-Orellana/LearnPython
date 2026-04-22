class perro:
    def __init__(self,nombre,raza):
        self.nombre=nombre
        self.raza=raza
    
    def mostrar(self):
        print(f"Mi perro se llama {self.nombre} y es de raza {self.raza}")


mi_perro = perro("Goofy","San Bernardo")

mi_perro.mostrar()