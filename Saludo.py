class PalindromeChecker:
    def __init__(self, text: str):
        self.text = text

    def is_palindrome(self) -> bool:
        """Verifica si la cadena es un palíndromo (ignora espacios y mayúsculas)."""
        cleaned = self.text.replace(" ", "").lower()
        return cleaned == cleaned[::-1]

# Ejemplo
checker = PalindromeChecker("Anita lava la tina")
print(checker.is_palindrome())  # True