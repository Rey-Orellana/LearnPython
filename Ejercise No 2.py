# DICCIONARIO: Colección no ordenada de pares clave: valor
# Las claves son únicas y permiten búsqueda rápida

# Crear un diccionario de estudiantes y sus notas
estudiantes = {
    "Ana": 8.5,
    "Luis": 7.0,
    "Carlos": 9.2
}

# Acceder a un valor por su clave
print(estudiantes["Ana"])  # Muestra 8.5
print(estudiantes.get("Luis"))  # Muestra 7.0

# Agregar o modificar un par
estudiantes["Diana"] = 9.8  # Agrega nueva estudiante
estudiantes["Luis"] = 7.5   # Modifica nota de Luis

# Verificar si una clave existe
if "Carlos" in estudiantes:
    print("Carlos está en el curso")

# Eliminar un par por su clave
del estudiantes["Ana"]

# Recorrer claves y valores
for nombre, nota in estudiantes.items():
    print(f"{nombre} sacó {nota}")

# Obtener solo las claves
print(estudiantes.keys())   # dict_keys(['Luis', 'Carlos', 'Diana'])

# Obtener solo los valores
print(estudiantes.values()) # dict_values([7.5, 9.2, 9.8])