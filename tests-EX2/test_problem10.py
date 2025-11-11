import pytest

from src.solutions.problem10 import second_largest


@pytest.mark.parametrize(
    "nums, expected",
    [
        ([1, 2, 3, 4, 5], 4),
        ([10, 10, 9], 9),
        ([-1, -2, -3], -2),
        ([5, 5, 5, 4], 4),
    ],
)
def test_second_largest(nums: list[int], expected: int) -> None:
    assert second_largest(nums) == expected


def test_second_largest_requires_two_unique_values() -> None:
    with pytest.raises(ValueError):
        second_largest([5, 5, 5])

