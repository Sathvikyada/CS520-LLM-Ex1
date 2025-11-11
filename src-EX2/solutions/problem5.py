def count_vowels(s: str) -> int:
    """Return the number of vowels (a, e, i, o, u) in ``s`` ignoring case."""
    vowels = "aeiou"
    return sum(1 for ch in s.lower() if ch in vowels)

