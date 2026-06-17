"""
Problem: Title Case Converter
Category: Strings
Date: 2026-06-17

Description:
    Convert a string to title case without using the built-in title() method.
"""


def to_title_case(s: str) -> str:
    """Convert string to title case manually."""
    if not s:
        return ""
    words = s.split()
    result = []
    for word in words:
        if word:
            result.append(word[0].upper() + word[1:].lower())
    return ' '.join(result)


# ── Tests ──
if __name__ == "__main__":
    assert to_title_case("hello world") == "Hello World"
    assert to_title_case("PYTHON IS FUN") == "Python Is Fun"
    assert to_title_case("a") == "A"
    assert to_title_case("") == ""
    print(f"All tests passed for: Title Case Converter")
