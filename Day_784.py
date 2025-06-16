

from itertools import starmap

def add_two(a,b):
    return(a+b)

my_list = [(1,1),(100,100)]

result = list(starmap(add_two,my_list))
print(result)

result2 = [add_two(x,y) for x,y in my_list]
print(result2)


