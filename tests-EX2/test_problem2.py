import pytest

from src.solutions.problem2 import is_palindrome


@pytest.mark.parametrize(
    "s, expected",
    [
        ("racecar", True),
        ("hello", False),
        ("A man a plan a canal Panama", True),
        ("", True),
        ("No lemon, no melon", True),
    ],
)
def test_is_palindrome(s: str, expected: bool) -> None:
    assert is_palindrome(s) is expected

