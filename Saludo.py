class VowelConsonantCounter:
    def __init__(self, text: str):
        self.text = text.lower()

    def count(self):
        vowels = "aeiou"
        num_vowels = sum(1 for ch in self.text if ch in vowels)
        num_consonants = sum(1 for ch in self.text if ch.isalpha() and ch not in vowels)
        return num_vowels, num_consonants

# Ejemplo
counter = VowelConsonantCounter("Hola Mundo")
voc, cons = counter.count()
print(f"Vocales: {voc}, Consonantes: {cons}")  # Vocales: 4, Consonantes: 5