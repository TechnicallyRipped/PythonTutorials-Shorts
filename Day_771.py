


def count_to_three():
    yield 1
    yield 2
    yield 3

my_gen = count_to_three()

print(my_gen)
print(next(my_gen))
print(next(my_gen))
print(next(my_gen))
print(next(my_gen))


