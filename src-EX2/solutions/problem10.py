from typing import List


def second_largest(nums: List[int]) -> int:
    """Return the second largest unique value in ``nums``."""
    unique_nums = sorted(set(nums))
    if len(unique_nums) < 2:
        raise ValueError("List must contain at least two unique numbers.")
    return unique_nums[-2]

