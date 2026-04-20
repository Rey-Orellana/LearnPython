class Motor:
    def __init__(self, tipo):
        self.tipo = tipo

    def encender(self):
        return f"Motor {self.tipo} rugiendo..."

class Auto:
    def __init__(self, marca, motor):
        self.marca = marca
        self.motor = motor  # El auto "tiene un" motor (Composición)

    def arrancar(self):
        return f"{self.marca}: {self.motor.encender()}"

# Creamos las piezas por separado
mi_motor = Motor("V8")
mi_nave = Auto("Ford", mi_motor)

print(mi_nave.arrancar())