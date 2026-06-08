"""
Problem: Insertion Sort
Category: Sorting
Date: 2026-06-08

Description:
    Implement the insertion sort algorithm.
"""


def insertion_sort(arr: list) -> list:
    """Sort a list using insertion sort algorithm."""
    arr = arr[:]
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
    return arr


# ── Tests ──
if __name__ == "__main__":
    assert insertion_sort([12, 11, 13, 5, 6]) == [5, 6, 11, 12, 13]
    assert insertion_sort([1]) == [1]
    assert insertion_sort([]) == []
    assert insertion_sort([2, 1]) == [1, 2]
    print(f"All tests passed for: Insertion Sort")
