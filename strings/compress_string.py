"""
Problem: String Compression
Category: Strings
Date: 2026-05-10

Description:
    Implement basic string compression using counts of repeated characters.
"""


def compress_string(s: str) -> str:
    """Compress string using run-length encoding."""
    if not s:
        return ""
    result = []
    count = 1
    for i in range(1, len(s)):
        if s[i] == s[i-1]:
            count += 1
        else:
            result.append(f"{s[i-1]}{count}")
            count = 1
    result.append(f"{s[-1]}{count}")
    compressed = ''.join(result)
    return compressed if len(compressed) < len(s) else s


# ── Tests ──
if __name__ == "__main__":
    assert compress_string("aabcccccaaa") == "a2b1c5a3"
    assert compress_string("abc") == "abc"
    assert compress_string("aabb") == "aabb"
    assert compress_string("") == ""
    print(f"All tests passed for: String Compression")
