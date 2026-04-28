import json

data = {"usuario": "admin", "puntos": 1500}

with open("datos.json", "w") as file:
    json.dump(data, file)