"""
Problem: Anagram Check
Category: Strings
Date: 2026-05-31

Description:
    Check if two strings are anagrams of each other.
"""


def is_anagram(s1: str, s2: str) -> bool:
    """Check if two strings are anagrams (case-insensitive)."""
    clean1 = sorted(s1.lower().replace(" ", ""))
    clean2 = sorted(s2.lower().replace(" ", ""))
    return clean1 == clean2


# ── Tests ──
if __name__ == "__main__":
    assert is_anagram("listen", "silent") == True
    assert is_anagram("Hello", "World") == False
    assert is_anagram("Dormitory", "Dirty Room") == True
    assert is_anagram("a", "a") == True
    print(f"All tests passed for: Anagram Check")
