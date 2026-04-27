class StringFormatter:
    def __init__(self, text: str):
        self.text = text

    def to_upper(self) -> str:
        return self.text.upper()

    def to_lower(self) -> str:
        return self.text.lower()

    def to_title(self) -> str:
        return self.text.title()

# Ejemplo
formatter = StringFormatter("el lenguaje PYTHON es GENIAL")
print(formatter.to_title())  # El Lenguaje Python Es Genial