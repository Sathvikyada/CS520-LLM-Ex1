import pytest

from src.solutions.problem7 import reverse_words


@pytest.mark.parametrize(
    "sentence, expected",
    [
        ("I love Python", "Python love I"),
        ("AI", "AI"),
        ("", ""),
        ("Data Science Rocks", "Rocks Science Data"),
    ],
)
def test_reverse_words(sentence: str, expected: str) -> None:
    assert reverse_words(sentence) == expected

