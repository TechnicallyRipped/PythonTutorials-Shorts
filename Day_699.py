


def divide_nums(x,y):
    try:
        return x/y
    except ZeroDivisionError:
        return "Input contains 0!"

a = divide_nums(10,0)
print(a)









