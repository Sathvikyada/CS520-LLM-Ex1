import pytest

from src.solutions.problem9 import merge_dicts


@pytest.mark.parametrize(
    "d1, d2, expected",
    [
        ({"a": 1}, {"b": 2}, {"a": 1, "b": 2}),
        ({"a": 2}, {"a": 3}, {"a": 5}),
        ({}, {"z": 9}, {"z": 9}),
        ({"x": 5, "y": 1}, {"y": 4, "z": 3}, {"x": 5, "y": 5, "z": 3}),
    ],
)
def test_merge_dicts(d1: dict[str, int], d2: dict[str, int], expected: dict[str, int]) -> None:
    assert merge_dicts(d1, d2) == expected

