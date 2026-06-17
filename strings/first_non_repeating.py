"""
Problem: First Non-Repeating Character
Category: Strings
Date: 2026-06-17

Description:
    Find the first non-repeating character in a string.
"""


def first_non_repeating(s: str) -> str:
    """Find first character that doesn't repeat in the string."""
    char_count = {}
    for char in s:
        char_count[char] = char_count.get(char, 0) + 1
    for char in s:
        if char_count[char] == 1:
            return char
    return None


# ── Tests ──
if __name__ == "__main__":
    assert first_non_repeating("aabbcdd") == "c"
    assert first_non_repeating("abcabc") == None
    assert first_non_repeating("a") == "a"
    assert first_non_repeating("aabbc") == "c"
    print(f"All tests passed for: First Non-Repeating Character")
