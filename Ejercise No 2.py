# PRINT: Muestra texto o variables en la consola

# Mostrar texto simple
print("Hola mundo")

# Mostrar variables
nombre = "Ana"
edad = 25
print(nombre, edad)  # Ana 25

# Concatenar con f-strings (recomendado)
print(f"Me llamo {nombre} y tengo {edad} años")

# Personalizar separador (por defecto es espacio)
print("uno", "dos", "tres", sep="-")  # uno-dos-tres

# Personalizar final (por defecto es salto de línea)
print("Hola", end=" ")
print("mundo")  # Hola mundo (en la misma línea)