def fibonaci(n, a=1, b=1):
    for i in range(n):
        a, b = b, a+b
    return a

#print(fibonaci(6))


def fib(n, a=1, b=1):
    for i in range(n):
        c = a
        a = b
        b = c+b
    return a

#print(fib(100000))