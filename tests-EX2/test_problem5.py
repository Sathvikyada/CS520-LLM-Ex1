import pytest

from src.solutions.problem5 import count_vowels


@pytest.mark.parametrize(
    "s, expected",
    [
        ("apple", 2),
        ("sky", 0),
        ("AEIOU", 5),
        ("", 0),
    ],
)
def test_count_vowels(s: str, expected: int) -> None:
    assert count_vowels(s) == expected

