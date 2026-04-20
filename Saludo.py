class CocheElectrico(Vehiculo): # Hereda de Vehiculo
    def __init__(self, marca, modelo, bateria):
        super().__init__(marca, modelo) # Llama al constructor del padre
        self.bateria = bateria

    def mostrar_bateria(self):
        return f"Batería al {self.bateria}%."

teslita = CocheElectrico("Tesla", "Model 3", 90)
print(teslita.describir())
print(teslita.mostrar_bateria())