


from itertools import dropwhile

def is_positive(num):
    return num > 0

x = [2, 1, -4, 8, -5]

result = list(dropwhile(is_positive,x))
print(result)
