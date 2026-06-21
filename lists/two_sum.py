"""
Problem: Two Sum
Category: Lists
Date: 2026-06-21

Description:
    Find indices of two numbers that add up to the target.
"""


def two_sum(nums: list, target: int) -> list:
    """Find two indices whose values sum to target."""
    seen = {}
    for i, num in enumerate(nums):
        complement = target - num
        if complement in seen:
            return [seen[complement], i]
        seen[num] = i
    return []


# ── Tests ──
if __name__ == "__main__":
    assert two_sum([2, 7, 11, 15], 9) == [0, 1]
    assert two_sum([3, 2, 4], 6) == [1, 2]
    assert two_sum([1, 2, 3], 10) == []
    print(f"All tests passed for: Two Sum")
