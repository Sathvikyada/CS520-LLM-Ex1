import pytest

from src.solutions.problem4 import factorial


@pytest.mark.parametrize(
    "n, expected",
    [
        (0, 1),
        (1, 1),
        (5, 120),
        (7, 5040),
    ],
)
def test_factorial(n: int, expected: int) -> None:
    assert factorial(n) == expected


def test_factorial_negative() -> None:
    with pytest.raises(ValueError):
        factorial(-1)

