# CONJUNTO: Colección no ordenada de elementos únicos (sin repetidos)
# Útil para eliminar duplicados y operaciones de teoría de conjuntos

# Crear un conjunto con números (los repetidos se eliminan automáticamente)
numeros = {1, 2, 3, 2, 4, 3, 5}
print(numeros)  # {1, 2, 3, 4, 5} - los duplicados desaparecieron

# Agregar elementos
numeros.add(6)
numeros.add(3)  # No hace nada porque 3 ya existe
print(numeros)  # {1, 2, 3, 4, 5, 6}

# Eliminar un elemento (si no existe da error)
numeros.remove(4)

# Eliminar sin error si no existe
numeros.discard(10)  # No pasa nada

# Unión de conjuntos (todos los elementos de ambos)
a = {1, 2, 3}
b = {3, 4, 5}
union = a | b  # o a.union(b)
print("Unión:", union)  # {1, 2, 3, 4, 5}

# Intersección (elementos que están en ambos)
interseccion = a & b  # o a.intersection(b)
print("Intersección:", interseccion)  # {3}

# Diferencia (elementos de a que no están en b)
diferencia = a - b  # o a.difference(b)
print("Diferencia (a - b):", diferencia)  # {1, 2}

# Convertir una lista con duplicados a conjunto (para limpiar)
lista_con_repetidos = [1, 2, 2, 3, 3, 3, 4]
sin_repetidos = set(lista_con_repetidos)
print("Lista original:", lista_con_repetidos)
print("Sin repetidos:", sin_repetidos)  # {1, 2, 3, 4}