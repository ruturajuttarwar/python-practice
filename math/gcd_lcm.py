"""
Problem: GCD and LCM
Category: Math
Date: 2026-05-29

Description:
    Compute the Greatest Common Divisor and Least Common Multiple.
"""


def gcd(a: int, b: int) -> int:
    """Compute GCD using Euclidean algorithm."""
    while b:
        a, b = b, a % b
    return a

def lcm(a: int, b: int) -> int:
    """Compute LCM using GCD."""
    return abs(a * b) // gcd(a, b)


# ── Tests ──
if __name__ == "__main__":
    assert gcd(12, 8) == 4
    assert gcd(17, 5) == 1
    assert lcm(4, 6) == 12
    assert lcm(3, 7) == 21
    print(f"All tests passed for: GCD and LCM")
