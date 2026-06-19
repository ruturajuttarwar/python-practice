"""
Problem: Prime Number Check
Category: Math
Date: 2026-06-19

Description:
    Check if a number is prime.
"""


def is_prime(n: int) -> bool:
    """Check if a number is prime."""
    if n < 2:
        return False
    if n < 4:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True


# ── Tests ──
if __name__ == "__main__":
    assert is_prime(2) == True
    assert is_prime(17) == True
    assert is_prime(1) == False
    assert is_prime(4) == False
    assert is_prime(97) == True
    print(f"All tests passed for: Prime Number Check")
