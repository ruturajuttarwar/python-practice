"""
Problem: Check Palindrome
Category: Strings
Date: 2026-06-15

Description:
    Check if a given string is a palindrome (case-insensitive).
"""


def is_palindrome(s: str) -> bool:
    """Check if string is a palindrome, ignoring case and spaces."""
    cleaned = ''.join(c.lower() for c in s if c.isalnum())
    left, right = 0, len(cleaned) - 1
    while left < right:
        if cleaned[left] != cleaned[right]:
            return False
        left += 1
        right -= 1
    return True


# ── Tests ──
if __name__ == "__main__":
    assert is_palindrome("racecar") == True
    assert is_palindrome("Race Car") == True
    assert is_palindrome("hello") == False
    assert is_palindrome("A man a plan a canal Panama") == True
    print(f"All tests passed for: Check Palindrome")
