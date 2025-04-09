def fibonacci() -> int:
    a, b = 0, 1

    while True:
        yield a
        a, b = b, a + b


# Example usage:
fibonacci_1 = fibonacci()
print(next(fibonacci_1))
print(next(fibonacci_1))
print(next(fibonacci_1))
print(next(fibonacci_1))
print(next(fibonacci_1))
print(next(fibonacci_1))
print(next(fibonacci_1))
