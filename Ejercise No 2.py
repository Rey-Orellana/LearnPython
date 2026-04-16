class Empleado:
    def __init__(self, nombre, sueldo):
        self.nombre = nombre
        self.sueldo = sueldo

class Gerente(Empleado):
    def __init__(self, nombre, sueldo, departamento):
        super().__init__(nombre, sueldo) # Reutiliza el init del padre
        self.departamento = departamento

boss = Gerente("Ana", 5000, "Ventas")
print(f"{boss.nombre} dirige {boss.departamento}")