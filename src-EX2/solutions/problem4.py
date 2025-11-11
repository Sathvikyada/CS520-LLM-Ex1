def factorial(n: int) -> int:
    """Return ``n!`` computed recursively, raising ``ValueError`` for negative inputs."""
    if n < 0:
        raise ValueError("Factorial is not defined for negative numbers.")
    if n <= 1:
        return 1
    return n * factorial(n - 1)

