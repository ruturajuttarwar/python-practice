"""
Problem: Sum of Digits
Category: Math
Date: 2026-06-03

Description:
    Compute the sum of digits of a number recursively.
"""


def digit_sum(n: int) -> int:
    """Recursively sum all digits of a number."""
    n = abs(n)
    if n < 10:
        return n
    return n % 10 + digit_sum(n // 10)


# ── Tests ──
if __name__ == "__main__":
    assert digit_sum(123) == 6
    assert digit_sum(9999) == 36
    assert digit_sum(0) == 0
    assert digit_sum(-456) == 15
    print(f"All tests passed for: Sum of Digits")
