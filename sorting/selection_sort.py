"""
Problem: Selection Sort
Category: Sorting
Date: 2026-05-28

Description:
    Implement the selection sort algorithm.
"""


def selection_sort(arr: list) -> list:
    """Sort a list using selection sort algorithm."""
    arr = arr[:]
    n = len(arr)
    for i in range(n):
        min_idx = i
        for j in range(i + 1, n):
            if arr[j] < arr[min_idx]:
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]
    return arr


# ── Tests ──
if __name__ == "__main__":
    assert selection_sort([64, 25, 12, 22, 11]) == [11, 12, 22, 25, 64]
    assert selection_sort([1]) == [1]
    assert selection_sort([]) == []
    assert selection_sort([3, 1, 2]) == [1, 2, 3]
    print(f"All tests passed for: Selection Sort")
