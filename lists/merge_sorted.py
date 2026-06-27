"""
Problem: Merge Sorted Lists
Category: Lists
Date: 2026-06-27

Description:
    Merge two sorted lists into one sorted list.
"""


def merge_sorted(list1: list, list2: list) -> list:
    """Merge two sorted lists into one sorted list."""
    result = []
    i = j = 0
    while i < len(list1) and j < len(list2):
        if list1[i] <= list2[j]:
            result.append(list1[i])
            i += 1
        else:
            result.append(list2[j])
            j += 1
    result.extend(list1[i:])
    result.extend(list2[j:])
    return result


# ── Tests ──
if __name__ == "__main__":
    assert merge_sorted([1, 3, 5], [2, 4, 6]) == [1, 2, 3, 4, 5, 6]
    assert merge_sorted([], [1, 2]) == [1, 2]
    assert merge_sorted([1], []) == [1]
    assert merge_sorted([], []) == []
    print(f"All tests passed for: Merge Sorted Lists")
