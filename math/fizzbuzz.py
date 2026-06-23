"""
Problem: FizzBuzz
Category: Math
Date: 2026-06-23

Description:
    Write a function that returns FizzBuzz output for numbers 1 to n.
"""


def fizzbuzz(n: int) -> list:
    """Classic FizzBuzz from 1 to n."""
    result = []
    for i in range(1, n + 1):
        if i % 15 == 0:
            result.append("FizzBuzz")
        elif i % 3 == 0:
            result.append("Fizz")
        elif i % 5 == 0:
            result.append("Buzz")
        else:
            result.append(str(i))
    return result


# ── Tests ──
if __name__ == "__main__":
    assert fizzbuzz(5) == ["1", "2", "Fizz", "4", "Buzz"]
    assert fizzbuzz(15)[-1] == "FizzBuzz"
    assert len(fizzbuzz(100)) == 100
    print(f"All tests passed for: FizzBuzz")
