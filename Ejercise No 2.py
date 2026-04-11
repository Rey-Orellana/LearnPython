# TYPE: Devuelve el tipo de dato de una variable

# Tipos comunes
nombre = "Juan"
edad = 30
altura = 1.75
es_mayor = True
colores = ["rojo", "verde"]

print(type(nombre))   # <class 'str'>
print(type(edad))     # <class 'int'>
print(type(altura))   # <class 'float'>
print(type(es_mayor)) # <class 'bool'>
print(type(colores))  # <class 'list'>

# Útil para depuración
valor = input("Ingresa algo: ")
print(f"El tipo de lo que ingresaste es: {type(valor)}")