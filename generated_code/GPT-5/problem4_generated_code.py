def factorial(n: int) -> int:
    # Step 1: Handle invalid input
    if n < 0:
        raise ValueError("Factorial is not defined for negative numbers.")
    
    # Step 2: Base case
    if n == 0 or n == 1:
        return 1
    
    # Step 3: Recursive case
    return n * factorial(n - 1)
