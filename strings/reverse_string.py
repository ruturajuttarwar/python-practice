"""
Problem: Reverse a String
Category: Strings
Date: 2026-05-21

Description:
    Write a function that reverses a given string without using slicing.
"""


def reverse_string(s: str) -> str:
    """Reverse a string without using slicing."""
    result = []
    for char in s:
        result.insert(0, char)
    return ''.join(result)


# ── Tests ──
if __name__ == "__main__":
    assert reverse_string("hello") == "olleh"
    assert reverse_string("Python") == "nohtyP"
    assert reverse_string("") == ""
    assert reverse_string("a") == "a"
    print(f"All tests passed for: Reverse a String")
