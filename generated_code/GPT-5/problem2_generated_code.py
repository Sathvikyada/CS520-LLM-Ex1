def is_palindrome(s: str) -> bool:
    # Step 1: Convert to lowercase
    s = s.lower()
    
    # Step 2: Keep only alphanumeric characters
    cleaned = ''.join(ch for ch in s if ch.isalnum())
    
    # Step 3: Compare with its reverse
    return cleaned == cleaned[::-1]
