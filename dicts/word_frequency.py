"""
Problem: Word Frequency Counter
Category: Dicts
Date: 2026-06-28

Description:
    Count the frequency of each word in a given text.
"""


def word_frequency(text: str) -> dict:
    """Count frequency of each word in text."""
    words = text.lower().split()
    freq = {}
    for word in words:
        cleaned = ''.join(c for c in word if c.isalnum())
        if cleaned:
            freq[cleaned] = freq.get(cleaned, 0) + 1
    return freq


# ── Tests ──
if __name__ == "__main__":
    assert word_frequency("the cat and the dog") == {"the": 2, "cat": 1, "and": 1, "dog": 1}
    assert word_frequency("hello hello hello") == {"hello": 3}
    assert word_frequency("") == {}
    print(f"All tests passed for: Word Frequency Counter")
