class Empleado:
    def __init__(self, nombre, sueldo):
        self.nombre = nombre
        self.__sueldo = sueldo

    @property
    def sueldo(self):
        return f"$ {self.__sueldo}"

    @sueldo.setter
    def sueldo(self, nuevo_sueldo):
        if nuevo_sueldo > 0:
            self.__sueldo = nuevo_sueldo
        else:
            print("Error: El sueldo debe ser positivo.")

emp = Empleado("Luis", 2000)
print(emp.sueldo)   # Se accede como atributo, no como función emp.sueldo()
emp.sueldo = 2500   # Se usa el setter para validar