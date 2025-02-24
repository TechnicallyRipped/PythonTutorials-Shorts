




from itertools import chain

x = [1,2,3]
y = (4,5,6)
z = 'abc'

for item in chain(x,y,z):
    print(item)
