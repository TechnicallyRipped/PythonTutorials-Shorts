



from functools import partial

def multiply(x, y):
    return x * y

# multiply(10,2)

double = partial(multiply, y=2)
doubled = double(x=10)
print(doubled)

triple = partial(multiply, y=3)
tripled = triple(10)
print(tripled)














