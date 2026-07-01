"""
Problem: Factorial Calculator
Category: Math
Date: 2026-07-01

Description:
    Write both iterative and recursive implementations of factorial.
"""


def factorial_iterative(n: int) -> int:
    """Calculate factorial iteratively."""
    if n < 0:
        raise ValueError("Factorial not defined for negative numbers")
    result = 1
    for i in range(2, n + 1):
        result *= i
    return result

def factorial_recursive(n: int) -> int:
    """Calculate factorial recursively."""
    if n < 0:
        raise ValueError("Factorial not defined for negative numbers")
    if n <= 1:
        return 1
    return n * factorial_recursive(n - 1)


# ── Tests ──
if __name__ == "__main__":
    assert factorial_iterative(5) == 120
    assert factorial_iterative(0) == 1
    assert factorial_recursive(5) == 120
    assert factorial_recursive(0) == 1
    print(f"All tests passed for: Factorial Calculator")
