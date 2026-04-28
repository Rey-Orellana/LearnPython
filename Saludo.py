import json

data = {"z": 1, "a": 2, "m": 3}
ordered_json = json.dumps(data, indent=4, sort_keys=True)

print(ordered_json)