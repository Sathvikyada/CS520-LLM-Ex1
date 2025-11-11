import pytest

from src.solutions.problem8 import is_prime


@pytest.mark.parametrize(
    "n, expected",
    [
        (2, True),
        (9, False),
        (13, True),
        (1, False),
        (0, False),
    ],
)
def test_is_prime(n: int, expected: bool) -> None:
    assert is_prime(n) is expected


def test_is_prime_even_composite() -> None:
    assert is_prime(4) is False


def test_is_prime_negative_number() -> None:
    assert is_prime(-7) is False


def test_is_prime_large_prime() -> None:
    assert is_prime(97) is True


def test_is_prime_square_of_prime() -> None:
    assert is_prime(121) is False


def test_is_prime_carmichael_number() -> None:
    assert is_prime(561) is False

