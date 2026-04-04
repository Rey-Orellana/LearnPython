##Comentarios en Python
#en Python se imprimero con la fguncion Print
print("Me gusta la pizza..!!!")


##Variables en Python


nombre = "Rey"

apellido = "Orellana"
estatura = 1.80

sexo = 'M'

estudiante = False

valor = ""
if(estudiante):
    valor = " estudiante"
else:
    valor = " pandillero"

print(f"Hola como estas {nombre} {apellido} eres {valor} eres de sexo {sexo} y mides {estatura}")



#Como ver los tipos de datos de las variables

print(type(nombre))
print(type(estatura))
print(type(sexo))
print(type(estudiante))