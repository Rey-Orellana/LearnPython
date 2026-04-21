class CuentaBancaria:
    def __init__(self, saldo):
        self.__saldo = saldo # Atributo privado

    def ver_saldo(self):
        return f"Tu saldo es ${self.__saldo}"

cuenta = CuentaBancaria(1000)
print(cuenta.ver_saldo())
# print(cuenta.__saldo) # Esto daría error