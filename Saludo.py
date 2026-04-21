class Animal:
    def respirar(self):
        print("Inhalando y exhalando...")

class Pez(Animal): # Pez hereda de Animal
    def nadar(self):
        print("Glup glup, estoy nadando")

nemo = Pez()
nemo.respirar() # ¡Puede respirar porque es un animal!
nemo.nadar()