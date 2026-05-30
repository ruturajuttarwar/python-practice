"""
Problem: Remove Duplicates
Category: Lists
Date: 2026-05-30

Description:
    Remove duplicates from a list while preserving order.
"""


def remove_duplicates(lst: list) -> list:
    """Remove duplicates while preserving order."""
    seen = set()
    result = []
    for item in lst:
        if item not in seen:
            seen.add(item)
            result.append(item)
    return result


# ── Tests ──
if __name__ == "__main__":
    assert remove_duplicates([1, 2, 2, 3, 3, 3]) == [1, 2, 3]
    assert remove_duplicates([1, 1, 1]) == [1]
    assert remove_duplicates([]) == []
    assert remove_duplicates([1, 2, 3]) == [1, 2, 3]
    print(f"All tests passed for: Remove Duplicates")
