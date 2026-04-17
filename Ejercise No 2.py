import json

estudiante = '{"Nombre":"Joaquin","Apellido":"Paco","Edad":35,"Estado":True}'

primero = json.dumps(estudiante)

print(primero)