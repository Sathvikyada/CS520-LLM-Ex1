def reverse_words(sentence: str) -> str:
    """
    Reverses the order of words in the input string.
    Words are separated by spaces. Multiple spaces are treated as one separator.
    
    Args:
        sentence: a string
    
    Returns:
        A string with the words in reversed order
    
    Examples:
        >>> reverse_words("I love Python")
        'Python love I'
    """
    # Split by whitespace (handles multiple spaces automatically)
    words = sentence.split()
    
    # Reverse the list of words
    reversed_words = words[::-1]
    
    # Join with single space
    return ' '.join(reversed_words)
