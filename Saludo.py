import json

data = {"nombre": "Alex", "edad": 25, "ciudad": "Madrid"}
json_string = json.dumps(data)

print(json_string)