class Lampara:
    def __init__(self):
        self.encendida = False

    def interruptor(self):
        self.encendida = not self.encendida
        estado = "encendida" if self.encendida else "apagada"
        print(f"La lámpara está {estado}")

foco = Lampara()
foco.interruptor()
foco.interruptor()