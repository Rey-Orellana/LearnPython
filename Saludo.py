import json

with open("datos.json", "r") as file:
    data = json.load(file)

print(data)