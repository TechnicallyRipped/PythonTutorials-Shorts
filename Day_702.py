


myList = ['A','B','C','A','A','B']
counts = {}

for item in myList:
    if item not in counts:
        counts[item] = 1
    else: 
        counts[item] += 1

print(counts)

