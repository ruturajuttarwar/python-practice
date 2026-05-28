"""
Problem: Power of Two
Category: Math
Date: 2026-05-28

Description:
    Check if a given number is a power of two using bit manipulation.
"""


def is_power_of_two(n: int) -> bool:
    """Check if n is a power of 2 using bit manipulation."""
    if n <= 0:
        return False
    return (n & (n - 1)) == 0


# ── Tests ──
if __name__ == "__main__":
    assert is_power_of_two(1) == True
    assert is_power_of_two(16) == True
    assert is_power_of_two(18) == False
    assert is_power_of_two(0) == False
    assert is_power_of_two(1024) == True
    print(f"All tests passed for: Power of Two")
