"""
Problem: Fibonacci Sequence
Category: Math
Date: 2026-05-24

Description:
    Return the first n Fibonacci numbers.
"""


def fibonacci(n: int) -> list:
    """Generate first n Fibonacci numbers."""
    if n <= 0:
        return []
    if n == 1:
        return [0]
    fibs = [0, 1]
    for _ in range(2, n):
        fibs.append(fibs[-1] + fibs[-2])
    return fibs


# ── Tests ──
if __name__ == "__main__":
    assert fibonacci(1) == [0]
    assert fibonacci(5) == [0, 1, 1, 2, 3]
    assert fibonacci(8) == [0, 1, 1, 2, 3, 5, 8, 13]
    assert fibonacci(0) == []
    print(f"All tests passed for: Fibonacci Sequence")
