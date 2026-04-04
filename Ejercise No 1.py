#Haciendo un carrito de compras en Python

item = input("Ingresa el producto que deseas adquirir: ")
precio = float(input(f"Cuanto es el precio del {item}: "))
cantidad = int(input(f"cual es la cantidad {item}: "))

operacionCarrito = float(cantidad*precio)

print(f"El total de {item}s es de {cantidad} por precio de unidad {precio}")
print(f"El total es de {round(operacionCarrito,2)}")
