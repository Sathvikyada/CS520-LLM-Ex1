def second_largest(nums: list[int]) -> int:
    unique_nums = list(set(nums))
    unique_nums.sort()
    return unique_nums[-2]
