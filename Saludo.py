class StringTrimmer:
    def __init__(self, text: str):
        self.text = text

    def clean(self) -> str:
        """Elimina espacios al inicio/final y reduce múltiples espacios internos."""
        return " ".join(self.text.split())

# Ejemplo
trimmer = StringTrimmer("   Python   es   genial   ")
print(trimmer.clean())  # "Python es genial"