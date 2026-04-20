class Pastel:
    def __init__(self, ingredientes):
        self.ingredientes = ingredientes

    @classmethod
    def pastel_chocolate(cls):
        return cls(['harina', 'leche', 'chocolate'])

    @staticmethod
    def es_apto_para_diabeticos(ingredientes):
        return 'azúcar' not in ingredientes

# Usando el método de clase para crear un objeto predefinido
mi_pastel = Pastel.pastel_chocolate()
print(mi_pastel.ingredientes)

# Usando el método estático sin crear una instancia
print(Pastel.es_apto_para_diabeticos(['harina', 'stevia']))