# LEN: Devuelve la cantidad de elementos en una secuencia o colección

# Con strings (cuenta caracteres)
texto = "Python"
print(len(texto))  # 6

# Con listas
frutas = ["manzana", "pera", "uva"]
print(len(frutas))  # 3

# Con diccionarios
alumnos = {"Ana": 8, "Luis": 7, "Carlos": 9}
print(len(alumnos))  # 3

# En condiciones (útil para validar)
if len(frutas) > 0:
    print("Hay frutas en la lista")