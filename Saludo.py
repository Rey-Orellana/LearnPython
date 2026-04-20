class Vehiculo:
    # El método __init__ es el constructor
    def __init__(self, marca, modelo):
        self.marca = marca    # Atributo de instancia
        self.modelo = modelo  # Atributo de instancia

    # Un método para definir un comportamiento
    def describir(self):
        return f"Este es un {self.marca} modelo {self.modelo}."

# Crear un objeto (instancia de la clase)
mi_auto = Vehiculo("Toyota", "Corolla")
print(mi_auto.describir())


class CocheElectrico(Vehiculo): # Hereda de Vehiculo
    def __init__(self, marca, modelo, bateria):
        super().__init__(marca, modelo) # Llama al constructor del padre
        self.bateria = bateria

    def mostrar_bateria(self):
        return f"Batería al {self.bateria}%."

teslita = CocheElectrico("Tesla", "Model 3", 90)
print(teslita.describir())
print(teslita.mostrar_bateria())