"""
Problem: Second Largest Element
Category: Lists
Date: 2026-05-28

Description:
    Find the second largest element without sorting.
"""


def second_largest(nums: list) -> int:
    """Find second largest element without sorting."""
    if len(nums) < 2:
        raise ValueError("Need at least 2 elements")
    first = second = float('-inf')
    for num in nums:
        if num > first:
            second = first
            first = num
        elif num > second and num != first:
            second = num
    if second == float('-inf'):
        raise ValueError("No second largest found")
    return second


# ── Tests ──
if __name__ == "__main__":
    assert second_largest([1, 5, 2, 8, 3]) == 5
    assert second_largest([10, 20]) == 10
    assert second_largest([1, 2, 3, 4, 5]) == 4
    print(f"All tests passed for: Second Largest Element")
