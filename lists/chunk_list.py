"""
Problem: Chunk List
Category: Lists
Date: 2026-05-06

Description:
    Split a list into chunks of a given size.
"""


def chunk_list(lst: list, size: int) -> list:
    """Split list into chunks of given size."""
    if size <= 0:
        raise ValueError("Chunk size must be positive")
    return [lst[i:i + size] for i in range(0, len(lst), size)]


# ── Tests ──
if __name__ == "__main__":
    assert chunk_list([1, 2, 3, 4, 5], 2) == [[1, 2], [3, 4], [5]]
    assert chunk_list([1, 2, 3], 1) == [[1], [2], [3]]
    assert chunk_list([1, 2, 3], 5) == [[1, 2, 3]]
    assert chunk_list([], 3) == []
    print(f"All tests passed for: Chunk List")
