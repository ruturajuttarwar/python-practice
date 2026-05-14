"""
Problem: Armstrong Number
Category: Math
Date: 2026-05-14

Description:
    Check if a number is an Armstrong number.
"""


def is_armstrong(n: int) -> bool:
    """Check if n is an Armstrong (narcissistic) number."""
    digits = str(abs(n))
    power = len(digits)
    total = sum(int(d) ** power for d in digits)
    return total == abs(n)


# ── Tests ──
if __name__ == "__main__":
    assert is_armstrong(153) == True
    assert is_armstrong(370) == True
    assert is_armstrong(9474) == True
    assert is_armstrong(123) == False
    print(f"All tests passed for: Armstrong Number")
