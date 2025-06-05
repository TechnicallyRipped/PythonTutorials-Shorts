


from itertools import tee

x = [1,2,3]

my_iter = iter(x)

a, b = tee(my_iter,2)

print(next(a))
print(next(a))
print(next(a))
print(next(b))
print(next(b))
print(next(b))









