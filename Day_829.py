
import json

name = "Mike"
age = 35
hobbies = ["Running", "Singing"]

data = {"name": name,
        "age": age,
        "hobbies": hobbies}

with open('dd.json', 'w') as f:
    json.dump(data, f, indent=2)
    