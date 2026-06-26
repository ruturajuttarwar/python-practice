"""
Problem: Matrix Transpose
Category: Utility
Date: 2026-06-26

Description:
    Transpose a matrix (list of lists).
"""


def transpose(matrix: list) -> list:
    """Transpose a matrix (list of lists)."""
    if not matrix:
        return []
    return [[row[i] for row in matrix] for i in range(len(matrix[0]))]


# ── Tests ──
if __name__ == "__main__":
    assert transpose([[1, 2], [3, 4]]) == [[1, 3], [2, 4]]
    assert transpose([[1, 2, 3]]) == [[1], [2], [3]]
    assert transpose([]) == []
    print(f"All tests passed for: Matrix Transpose")
