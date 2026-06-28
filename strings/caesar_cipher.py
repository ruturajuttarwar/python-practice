"""
Problem: Caesar Cipher
Category: Strings
Date: 2026-06-28

Description:
    Implement a Caesar cipher that shifts each letter by a given number of positions.
"""


def caesar_cipher(text: str, shift: int) -> str:
    """Encrypt text using Caesar cipher with given shift."""
    result = []
    for char in text:
        if char.isalpha():
            base = ord('A') if char.isupper() else ord('a')
            shifted = (ord(char) - base + shift) % 26 + base
            result.append(chr(shifted))
        else:
            result.append(char)
    return ''.join(result)


# ── Tests ──
if __name__ == "__main__":
    assert caesar_cipher("abc", 1) == "bcd"
    assert caesar_cipher("xyz", 3) == "abc"
    assert caesar_cipher("Hello, World!", 5) == "Mjqqt, Btwqi!"
    assert caesar_cipher("abc", 0) == "abc"
    print(f"All tests passed for: Caesar Cipher")
