#Clases en Python

class Vehiculo:
    def __init__(self, marca, modelo):
        self.marca = marca
        self.modelo = modelo
    
    def describir(self):
        return f"Este es un {self.marca} modelo {self.modelo}"
    

mi_auto = Vehiculo("Toyota","Corolla")
print(mi_auto.describir())