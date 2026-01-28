
from itertools import zip_longest

x = [1,2,3,4]
y = [5,10]

points = list(zip_longest(x,y,
                          fillvalue=100))

print(points)