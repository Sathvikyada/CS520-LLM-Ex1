def count_vowels(s: str) -> int:
    """
    Returns the number of vowels in a given string.
    
    Args:
        s: a string
    
    Returns:
        The count of vowels (case-insensitive)
    
    Examples:
        >>> count_vowels("apple")
        2
        >>> count_vowels("sky")
        0
    """
    # Define vowels (both lowercase and uppercase)
    vowels = "aeiouAEIOU"
    
    # Count characters that are vowels
    return sum(1 for char in s if char in vowels)
