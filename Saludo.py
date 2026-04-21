class Robot:
    total_robots = 0  # Atributo de clase

    def __init__(self, nombre):
        self.nombre = nombre
        Robot.total_robots += 1  # Cada que nace uno, sumamos

    @classmethod
    def imprimir_poblacion(cls):
        print(f"Hay {cls.total_robots} robots en el mundo.")

r1 = Robot("R2D2")
r2 = Robot("C3PO")
Robot.imprimir_poblacion()  # Salida: Hay 2 robots en el mundo.