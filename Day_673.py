



from itertools import chain

x = [[1,2],(3,4),5]

flattened = list(chain.from_iterable(x))
print(flattened)



