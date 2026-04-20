class CuentaBancaria:
    def __init__(self, saldo_inicial):
        self.__saldo = saldo_inicial  # Atributo privado

    def depositar(self, monto):
        if monto > 0:
            self.__saldo += monto
            print(f"Depósito exitoso. Nuevo saldo: {self.__saldo}")

    def obtener_saldo(self):
        return f"Saldo actual: {self.__saldo}"

cuenta = CuentaBancaria(1000)
cuenta.depositar(500)
# print(cuenta.__saldo)  # Esto lanzaría un error de atributo
print(cuenta.obtener_saldo())