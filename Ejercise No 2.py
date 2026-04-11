# INPUT: Recibe texto ingresado por el usuario (siempre devuelve string)

# Entrada básica
nombre = input("¿Cómo te llamas? ")
print(f"Hola {nombre}")

# Convertir a número (importante porque input devuelve texto)
edad_texto = input("¿Cuántos años tienes? ")
edad = int(edad_texto)  # Convertir a entero
print(f"El año que viene tendrás {edad + 1} años")

# Versión compacta
numero = int(input("Ingresa un número: "))
print(f"El doble es {numero * 2}")