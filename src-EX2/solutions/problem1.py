def sum_of_digits(n: int) -> int:
    """Return the sum of the digits in the integer ``n``."""
    return sum(int(digit) for digit in str(abs(n)))

