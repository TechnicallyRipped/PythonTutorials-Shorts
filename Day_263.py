

def fibonacci_sequence(f1,f2,n):
    fib_seq = [f1, f2]

    while len(fib_seq) < n:
        fib_seq.append(fib_seq[-1] + fib_seq[-2])

    return fib_seq

result = fibonacci_sequence(0,1,10)
print(result)



















