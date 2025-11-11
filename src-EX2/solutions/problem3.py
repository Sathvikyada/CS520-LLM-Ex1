def fibonacci(n: int) -> int:
    """Return the nth Fibonacci number for a 1-indexed sequence starting with 0, 1, 1, ..."""
    if n == 1:
        return 0
    if n == 2:
        return 1

    a, b = 0, 1
    for _ in range(3, n + 1):
        a, b = b, a + b
    return b

