def fibonacci(n: int) -> int:
    # Step 1: Handle base cases
    if n == 1:
        return 0
    elif n == 2:
        return 1
    
    # Step 2: Initialize first two Fibonacci numbers
    a, b = 0, 1
    
    # Step 3: Loop from 3 to n to build the sequence
    for _ in range(3, n + 1):
        a, b = b, a + b  # Update the two previous numbers
    
    # Step 4: Return the nth Fibonacci number
    return b
