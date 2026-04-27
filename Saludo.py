class StringReplacer:
    def __init__(self, text: str):
        self.text = text

    def replace_word(self, old: str, new: str) -> str:
        return self.text.replace(old, new)

# Ejemplo
replacer = StringReplacer("Me gusta Java")
nuevo_texto = replacer.replace_word("Java", "Python")
print(nuevo_texto)  # Me gusta Python