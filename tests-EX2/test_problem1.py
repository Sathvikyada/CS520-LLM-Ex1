import pytest

from src.solutions.problem1 import sum_of_digits


@pytest.mark.parametrize(
    "n, expected",
    [
        (123, 6),
        (0, 0),
        (99999, 45),
        (-987, 24),
    ],
)
def test_sum_of_digits(n: int, expected: int) -> None:
    assert sum_of_digits(n) == expected

