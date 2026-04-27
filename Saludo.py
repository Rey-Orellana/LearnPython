class EmailValidator:
    def __init__(self, email: str):
        self.email = email

    def is_valid(self) -> bool:
        """Validación simple: contiene '@' y un punto después de '@'."""
        if "@" not in self.email:
            return False
        local, domain = self.email.split("@")
        return len(local) > 0 and "." in domain and len(domain.split(".")[-1]) >= 2

# Ejemplo
validator = EmailValidator("usuario@example.com")
print(validator.is_valid())  # True