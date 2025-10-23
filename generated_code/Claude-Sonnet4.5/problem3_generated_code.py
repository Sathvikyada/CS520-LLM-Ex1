def fibonacci(n: int) -> int:
    """
    Returns the nth Fibonacci number using iteration.
    The sequence starts as 0, 1, 1, 2, 3, 5, 8...
    
    Args:
        n: a positive integer representing the position (1-indexed)
    
    Returns:
        The nth Fibonacci number
    
    Examples:
        >>> fibonacci(1)
        0
        >>> fibonacci(2)
        1
        >>> fibonacci(7)
        8
    """
    # Base cases
    if n == 1:
        return 0
    if n == 2:
        return 1
    
    # Initialize first two Fibonacci numbers
    prev2 = 0  # F(1)
    prev1 = 1  # F(2)
    
    # Iterate from position 3 to n
    for i in range(3, n + 1):
        current = prev1 + prev2
        # Shift the window forward
        prev2 = prev1
        prev1 = current
    
    return prev1
