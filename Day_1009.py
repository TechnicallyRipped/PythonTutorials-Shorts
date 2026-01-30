


from itertools import takewhile

def is_positive(num):
    return num > 0

x = [3,4,10,-2,20]

result = list(takewhile(is_positive,x))
print(result)