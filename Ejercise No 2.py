import json

x = '{"name" : "Jhon","age" : 30,"city" : "New York"}'

y = json.loads(x)

print(y["age"])