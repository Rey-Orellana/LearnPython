# PILA: El último elemento que entra es el primero en salir
# Ejemplo real: una pila de platos

pila = []

# Apilar (push) - agregar elementos
pila.append("Tarea 1")  # Primera tarea
pila.append("Tarea 2")  # Segunda tarea
pila.append("Tarea 3")  # Tercera tarea
print("Pila:", pila)  # ['Tarea 1', 'Tarea 2', 'Tarea 3']

# Desapilar (pop) - quitar el último elemento agregado
tarea_completada = pila.pop()  # Saca "Tarea 3"
print("Completada:", tarea_completada)
print("Pila después:", pila)  # ['Tarea 1', 'Tarea 2']

# Ver el último elemento sin quitarlo (peek)
ultima = pila[-1]
print("Última tarea pendiente:", ultima)  # Tarea 2

# Verificar si está vacía
if not pila:
    print("No hay tareas")
else:
    print("Tareas pendientes:", len(pila))  # 2 tareas