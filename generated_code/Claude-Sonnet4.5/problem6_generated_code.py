def find_max(nums: list[int]) -> int:
    """
    Returns the maximum value in a list without using the built-in max() function.
    
    Args:
        nums: a list of integers (non-empty)
    
    Returns:
        The largest integer in the list
    
    Examples:
        >>> find_max([1, 2, 3, 4, 5])
        5
    """
    # Initialize with the first element (handles negative numbers correctly)
    max_val = nums[0]
    
    # Compare with remaining elements
    for num in nums[1:]:
        if num > max_val:
            max_val = num
    
    return max_val
