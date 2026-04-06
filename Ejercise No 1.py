#Listas y metodos en Python

l = [1,2,3,4,5,6]

l.append(7)

print(l)

#Metodo para agregar de acuerdo a un indice con insert

l.insert(0,0)
print(l)

#Unir dos listas con extend

lista1 = ["uno","dos","tres"]
lista2 = ["cuatro","cinco","seis"]

lista1.extend(lista2)

print(lista1)

#Eliminar elementos en una lista

lista1.pop(0)

print(lista1)