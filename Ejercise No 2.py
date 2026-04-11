#Estructuras de datos en python
# LISTA: Colección ordenada y mutable que permite elementos duplicados

# Crear una lista de números
numeros = [10, 20, 30, 40, 50]

# Agregar un elemento al final
numeros.append(60)  # [10, 20, 30, 40, 50, 60]

# Insertar en una posición específica (índice 2, valor 25)
numeros.insert(2, 25)  # [10, 20, 25, 30, 40, 50, 60]

# Acceder a un elemento por su índice (el primer elemento es índice 0)
print(numeros[0])  # Muestra 10

# Eliminar un elemento por su valor
numeros.remove(40)  # [10, 20, 25, 30, 50, 60]

# Recorrer la lista con un bucle
for num in numeros:
    print(num, end=" ")  # Muestra: 10 20 25 30 50 60

# Obtener el largo (cantidad de elementos)
print("\nCantidad:", len(numeros))  # Muestra: 6