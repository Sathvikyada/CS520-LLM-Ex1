def merge_dicts(d1: dict, d2: dict) -> dict:
    """
    Merges two dictionaries and sums the values for any duplicate keys.
    Does not modify the original dictionaries.
    
    Args:
        d1, d2: dictionaries with string keys and integer values
    
    Returns:
        A new dictionary containing all keys from both,
        summing overlapping keys' values
    
    Examples:
        >>> merge_dicts({'a':1}, {'b':2})
        {'a': 1, 'b': 2}
        >>> merge_dicts({'a':2}, {'a':3})
        {'a': 5}
    """
    # Create a copy of d1 to avoid modifying the original
    result = d1.copy()
    
    # Add or sum values from d2
    for key, value in d2.items():
        if key in result:
            result[key] += value
        else:
            result[key] = value
    
    return result
