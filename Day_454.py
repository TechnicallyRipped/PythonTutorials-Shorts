


from itertools import dropwhile

x = [1, 2, 3, 1, 4, 5, 6]

y = list(dropwhile(lambda i: i < 3, x))
print(y)












