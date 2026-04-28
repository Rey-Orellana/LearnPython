import json

data = {"id": 1, "items": ["manzana", "pera"], "activo": True}
pretty_json = json.dumps(data, indent=4)

print(pretty_json)