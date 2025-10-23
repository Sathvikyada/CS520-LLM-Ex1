def sum_of_digits(n: int) -> int:
    # Take the absolute value of n to handle negatives
    n = abs(n)
    
    # Convert to string and sum each digit converted back to int
    total = sum(int(digit) for digit in str(n))
    
    return total