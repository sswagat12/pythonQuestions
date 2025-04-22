def prime_nums(n):
    primes = [x for x in range(2, n) if all(x%y != 0 for y in range(2,x))]
    return primes
print(prime_nums(100))