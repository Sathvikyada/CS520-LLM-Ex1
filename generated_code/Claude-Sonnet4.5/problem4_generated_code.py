
def factorial(n: int) -> int:
    """
    Returns the factorial of n using recursion.
    
    Args:
        n: a non-negative integer
    
    Returns:
        The factorial of n
    
    Examples:
        >>> factorial(0)
        1
        >>> factorial(5)
        120
    """
    # Base case: 0! = 1
    if n == 0:
        return 1
    
    # Recursive case: n! = n × (n-1)!
    return n * factorial(n - 1)
