import json

json_data = '{"nombre": "Alex", "edad": 25, "ciudad": "Madrid"}'
data = json.loads(json_data)

print(data["nombre"])  # Salida: Alex