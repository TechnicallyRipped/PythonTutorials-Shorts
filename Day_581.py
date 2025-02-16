

list1 = ['a','b','c']
list2 = [1,2,3]

result = []

for l in list1:
    for n in list2:
        result.append((l,n))

print(result)

result2 = [(l,n) for l in list1 for n in list2]

print(result2)



