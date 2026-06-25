"""
Problem: Flatten Nested List
Category: Lists
Date: 2026-06-25

Description:
    Flatten a nested list of arbitrary depth.
"""


def flatten(lst: list) -> list:
    """Flatten a nested list of arbitrary depth."""
    result = []
    for item in lst:
        if isinstance(item, list):
            result.extend(flatten(item))
        else:
            result.append(item)
    return result


# ── Tests ──
if __name__ == "__main__":
    assert flatten([1, [2, 3], [4, [5, 6]]]) == [1, 2, 3, 4, 5, 6]
    assert flatten([]) == []
    assert flatten([1, 2, 3]) == [1, 2, 3]
    assert flatten([[[[1]]]]) == [1]
    print(f"All tests passed for: Flatten Nested List")
