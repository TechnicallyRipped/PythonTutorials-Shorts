

import json

with open('j.json', 'r') as file:
    data = json.load(file)

print(data)
print(type(data))

print(data['Joe']['Age'])
