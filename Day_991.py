

data = ['a', 'b', 'b', 'c', 'c', 'c']

counts = {}

for x in data:
    counts[x] = counts.get(x, 0) + 1

# print(counts)

max_count = max(counts.values())

modes = []
for k, v in counts.items():
    if v == max_count:
        modes.append(k)

print(modes)
