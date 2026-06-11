"""
Problem: Bubble Sort
Category: Sorting
Date: 2026-06-11

Description:
    Implement the bubble sort algorithm.
"""


def bubble_sort(arr: list) -> list:
    """Sort a list using bubble sort algorithm."""
    arr = arr[:]
    n = len(arr)
    for i in range(n):
        swapped = False
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True
        if not swapped:
            break
    return arr


# ── Tests ──
if __name__ == "__main__":
    assert bubble_sort([64, 34, 25, 12, 22]) == [12, 22, 25, 34, 64]
    assert bubble_sort([1]) == [1]
    assert bubble_sort([]) == []
    assert bubble_sort([3, 2, 1]) == [1, 2, 3]
    print(f"All tests passed for: Bubble Sort")
