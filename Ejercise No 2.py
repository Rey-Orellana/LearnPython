class Pato:
    def hablar(self): return "Quack!"

class Gato:
    def hablar(self): return "Miau!"

def hacer_hablar(animal):
    print(animal.hablar())

hacer_hablar(Pato())
hacer_hablar(Gato())