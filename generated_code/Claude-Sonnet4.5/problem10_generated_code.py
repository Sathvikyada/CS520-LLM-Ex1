def second_largest(nums: list[int]) -> int:
    """
    Returns the second largest number in a list of integers.
    If there are duplicates of the maximum number, ignores them.
    
    Args:
        nums: list of integers with at least two unique numbers
    
    Returns:
        The second largest integer in the list
    
    Examples:
        >>> second_largest([1,2,3,4,5])
        4
        >>> second_largest([10,10,9])
        9
    """
    # Convert to set to remove duplicates, then back to sorted list
    unique_nums = sorted(set(nums), reverse=True)
    
    # Check if we have at least 2 unique values
    if len(unique_nums) < 2:
        raise ValueError("List must contain at least two unique numbers")
    
    # Return the second element (second largest)
    return unique_nums[1]
