def count_vowels(s: str) -> int:
    # Step 1: Define vowels
    vowels = "aeiou"
    
    # Step 2: Convert string to lowercase
    s = s.lower()
    
    # Step 3: Count how many characters are vowels
    count = sum(1 for ch in s if ch in vowels)
    
    return count
