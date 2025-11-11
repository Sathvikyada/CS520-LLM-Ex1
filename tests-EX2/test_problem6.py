import pytest

from src.solutions.problem6 import find_max


@pytest.mark.parametrize(
    "nums, expected",
    [
        ([1, 2, 3, 4, 5], 5),
        ([-1, -5, -2], -1),
        ([0], 0),
    ],
)
def test_find_max(nums: list[int], expected: int) -> None:
    assert find_max(nums) == expected


def test_find_max_raises_for_empty_list() -> None:
    with pytest.raises(ValueError):
        find_max([])


def test_find_max_all_negative_strictly_decreasing() -> None:
    assert find_max([-10, -30, -20, -50]) == -10


def test_find_max_large_magnitude_mix() -> None:
    assert find_max([10**6, -10**12, 10**3, 999_999]) == 10**6


def test_find_max_duplicate_max_values() -> None:
    assert find_max([42, 17, 42, 3]) == 42


def test_find_max_negative_and_positive_mix() -> None:
    assert find_max([-100, 0, -50, 75, 10]) == 75

