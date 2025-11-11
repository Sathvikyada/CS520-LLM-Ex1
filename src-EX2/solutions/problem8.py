def is_prime(n: int) -> bool:
    """Return True if ``n`` is prime, False otherwise."""
    if n <= 1:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False

    limit = int(n**0.5) + 1
    for candidate in range(3, limit, 2):
        if n % candidate == 0:
            return False
    return True

