# COLA: El primer elemento que entra es el primero en salir
# Ejemplo real: fila del supermercado

from collections import deque

cola = deque()

# Encolar - agregar al final
cola.append("Cliente 1")
cola.append("Cliente 2")
cola.append("Cliente 3")
print("Cola:", cola)  # deque(['Cliente 1', 'Cliente 2', 'Cliente 3'])

# Desencolar - atender al primero
atendido = cola.popleft()  # Saca "Cliente 1"
print("Atendido:", atendido)
print("Cola después:", cola)  # deque(['Cliente 2', 'Cliente 3'])

# Ver el primero sin quitarlo
siguiente = cola[0]
print("Próximo en atender:", siguiente)  # Cliente 2

# Recorrer la cola
for cliente in cola:
    print(f"Esperando: {cliente}")