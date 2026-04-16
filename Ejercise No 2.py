class Vehiculo:
    def mensaje(self):
        print("Este es un vehículo")

class Coche(Vehiculo): # Hereda de Vehiculo
    def tocar_bocina(self):
        print("¡Beep beep!")

mi_auto = Coche()
mi_auto.mensaje()      # Método heredado
mi_auto.tocar_bocina() # Método propio