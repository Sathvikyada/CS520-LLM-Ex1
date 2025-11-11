import pytest

from src.solutions.problem3 import fibonacci


@pytest.mark.parametrize(
    "n, expected",
    [
        (1, 0),
        (2, 1),
        (7, 8),
        (10, 34),
    ],
)
def test_fibonacci(n: int, expected: int) -> None:
    assert fibonacci(n) == expected

