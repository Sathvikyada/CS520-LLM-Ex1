def is_palindrome(s: str) -> bool:
    """Return True if ``s`` is a palindrome when ignoring non-alphanumeric characters and case."""
    cleaned = "".join(ch for ch in s.lower() if ch.isalnum())
    return cleaned == cleaned[::-1]

