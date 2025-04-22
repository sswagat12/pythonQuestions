def generate_fibonacci_series(n):
    a = 0
    b = 1
    fib_list = []
    for each in range(n):
        fib_list.append(a)
        a, b = b, a+b
    return fib_list
print(generate_fibonacci_series(5))
