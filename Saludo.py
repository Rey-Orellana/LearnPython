#Usando Json en Python

import json

x = {"nombre":"Mario","edad":30,"Ciudad":"Belin"}

y = json.loads(x)

print(y["edad"])