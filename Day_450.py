
from itertools import zip_longest
x = [1,2,3,4]
y = ['a','b']

# z = zip(x,y)

# print(list(z))

z2 = zip_longest(x,y,fillvalue=999)
print(list(z2))