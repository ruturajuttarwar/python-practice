"""
Problem: Rotate List
Category: Lists
Date: 2026-06-04

Description:
    Rotate a list by k positions to the right.
"""


def rotate_list(lst: list, k: int) -> list:
    """Rotate list by k positions to the right."""
    if not lst:
        return []
    k = k % len(lst)
    return lst[-k:] + lst[:-k] if k else lst[:]


# ── Tests ──
if __name__ == "__main__":
    assert rotate_list([1, 2, 3, 4, 5], 2) == [4, 5, 1, 2, 3]
    assert rotate_list([1, 2, 3], 0) == [1, 2, 3]
    assert rotate_list([1, 2, 3], 3) == [1, 2, 3]
    assert rotate_list([], 5) == []
    print(f"All tests passed for: Rotate List")
