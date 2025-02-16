

def isEven(n):
    if n == 0:
        print('Even')
    else:
        isOdd(n - 1)

def isOdd(n):
    if n == 0:
        print('Odd')
    else:
        isEven(n - 1)
    
isEven(9)