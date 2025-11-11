from typing import List


def find_max(nums: List[int]) -> int:
    """Return the largest value in ``nums`` without using ``max``."""
    if not nums:
        raise ValueError("nums must not be empty")

    max_val = nums[0]
    for n in nums[1:]:
        if n > max_val:
            max_val = n
    return max_val

