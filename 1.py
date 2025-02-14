import json

json_file = 'ferrari.json'

with open(json_file, 'r') as file:
    global ferrari
    ferrari = json.load(file)

print(type(ferrari))

print(ferrari)
print(ferrari["price"])