class StringReverser:
    def __init__(self, text: str):
        self.text = text

    def reverse(self) -> str:
        """Devuelve la cadena invertida."""
        return self.text[::-1]

# Ejemplo
reverser = StringReverser("Python")
print(reverser.reverse())  # nohtyP