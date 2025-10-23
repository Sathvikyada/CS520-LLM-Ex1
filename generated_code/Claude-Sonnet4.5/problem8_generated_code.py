import math

def is_prime(n: int) -> bool:
    """
    Returns True if the integer n is a prime number, and False otherwise.
    Optimized version that only checks up to sqrt(n).
    
    Args:
        n: an integer greater than or equal to 0
    
    Returns:
        True if n is prime, False otherwise
    
    Examples:
        >>> is_prime(2)
        True
        >>> is_prime(9)
        False
    """
    # Handle edge cases
    if n < 2:
        return False
    
    # 2 is the only even prime
    if n == 2:
        return True
    
    # All other even numbers are not prime
    if n % 2 == 0:
        return False
    
    # Check odd divisors from 3 to sqrt(n)
    # We only need to check up to sqrt(n) because if n = a * b,
    # then one of a or b must be <= sqrt(n)
    for i in range(3, int(math.sqrt(n)) + 1, 2):
        if n % i == 0:
            return False
    
    return True
