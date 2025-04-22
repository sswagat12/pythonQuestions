def fibonacci_generator():
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a + b

# Example usage
fib_gen = fibonacci_generator()
for _ in range(10):
    print(next(fib_gen)) 

print(f"next:::::;{next(fib_gen)}")