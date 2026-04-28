import json

data = {"mensaje": "HOLA, ¡niño!"}
# Sin False, verás códigos como \u00f1
print(json.dumps(data, ensure_ascii=False))