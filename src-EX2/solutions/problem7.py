def reverse_words(sentence: str) -> str:
    """Return ``sentence`` with word order reversed, collapsing whitespace."""
    words = sentence.split()
    return " ".join(reversed(words))

