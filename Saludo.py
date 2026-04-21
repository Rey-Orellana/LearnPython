class Gato:
    def __init__(self, nombre, color):
        self.nombre = nombre  # Atributo
        self.color = color    # Atributo

michi = Gato("Felix", "Naranja")
print(f"Mi gato se llama {michi.nombre} y es de color {michi.color}")