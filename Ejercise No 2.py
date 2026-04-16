class Robot:
    def __init__(self, nombre, modelo):
        self.nombre = nombre
        self.modelo = modelo

mi_robot = Robot("R2D2", "Astromecánico")
print(f"Hola, soy {mi_robot.nombre}")