def is_palindrome(s: str) -> bool:
    """
    Returns True if the given string is a palindrome, 
    ignoring spaces, punctuation, and case.
    
    Args:
        s: a string
    
    Returns:
        True if s is a palindrome, False otherwise
    
    Examples:
        >>> is_palindrome("racecar")
        True
        >>> is_palindrome("hello")
        False
        >>> is_palindrome("A man a plan a canal Panama")
        True
    """
    # Normalize: keep only alphanumeric characters and convert to lowercase
    cleaned = ''.join(char.lower() for char in s if char.isalnum())
    
    # Check if the cleaned string equals its reverse
    return cleaned == cleaned[::-1]
