"""
Problem: Binary Search
Category: Sorting
Date: 2026-07-02

Description:
    Implement binary search on a sorted list.
"""


def binary_search(arr: list, target: int) -> int:
    """Binary search — returns index or -1 if not found."""
    left, right = 0, len(arr) - 1
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return -1


# ── Tests ──
if __name__ == "__main__":
    assert binary_search([1, 3, 5, 7, 9], 5) == 2
    assert binary_search([1, 3, 5, 7, 9], 6) == -1
    assert binary_search([], 1) == -1
    assert binary_search([42], 42) == 0
    print(f"All tests passed for: Binary Search")
