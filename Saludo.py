class WordCounter:
    def __init__(self, text: str):
        self.text = text

    def count_words(self) -> int:
        """Cuenta palabras separadas por espacios."""
        return len(self.text.split())

# Ejemplo
counter = WordCounter("Aprender Python con POO es divertido")
print(counter.count_words())  # 6