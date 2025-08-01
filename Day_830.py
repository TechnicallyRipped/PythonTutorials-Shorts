

import json

data = []

with open("dd.jsonl", "r") as f:
    for line in f:
        data.append(json.loads(line))

print(data)
