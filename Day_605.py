


def is_even(i):
    return i % 2 == 0

x = [1,2,3,4,5,6]

y = list(filter(is_even, x))

print(y)

z = list(filter(lambda i: i%2 != 0,x))
print(z)





















