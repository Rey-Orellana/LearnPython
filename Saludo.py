class Motor:
    def encender(self):
        return "Motor haciendo Brum Brum!"

class Coche:
    def __init__(self, marca):
        self.marca = marca
        self.motor = Motor()  # El coche TIENE un motor

    def arrancar(self):
        print(f"El {self.marca} dice: {self.motor.encender()}")

mi_nave = Coche("Toyota")
mi_nave.arrancar()