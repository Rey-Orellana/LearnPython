#Carrito de compras

item = input("Ingresa el nombre del producto: ")

precio = float(input(f"Ingresa el precio del producto {item}: "))

cantidad = int(input(f"Ingresa la cantidad del prodcuto {item}: "))


total =precio*cantidad

print(f"El total a cancelar es de {total} por {cantidad} de {item}")