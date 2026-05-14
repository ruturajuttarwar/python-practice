"""
Problem: Count Vowels
Category: Strings
Date: 2026-05-14

Description:
    Count the number of vowels in a string.
"""


def count_vowels(s: str) -> int:
    """Count the number of vowels in a string."""
    vowels = set('aeiouAEIOU')
    return sum(1 for char in s if char in vowels)


# ── Tests ──
if __name__ == "__main__":
    assert count_vowels("hello") == 2
    assert count_vowels("AEIOU") == 5
    assert count_vowels("rhythm") == 0
    assert count_vowels("") == 0
    print(f"All tests passed for: Count Vowels")
