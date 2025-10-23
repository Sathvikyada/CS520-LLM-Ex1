def sum_of_digits(n: int) -> int:
    """
    Returns the sum of all digits in the integer n.
    
    Args:
        n: an integer (can be positive, zero, or negative)
    
    Returns:
        The sum of digits of the absolute value of n
    
    Examples:
        >>> sum_of_digits(123)
        6
        >>> sum_of_digits(0)
        0
        >>> sum_of_digits(-456)
        15
    """
    # Convert to absolute value to handle negative numbers
    # Then convert to string to easily iterate through digits
    return sum(int(digit) for digit in str(abs(n)))
