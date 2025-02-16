


def reverse_int(x):
    negative = x < 0

    x = int(str(abs(x))[::-1])

    if negative:
        x = -x
        
    return x





print(reverse_int(-95))

















