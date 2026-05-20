"""
Problem: Invert Dictionary
Category: Dicts
Date: 2026-05-20

Description:
    Swap keys and values of a dictionary.
"""


def invert_dict(d: dict) -> dict:
    """Invert a dictionary, collecting keys for duplicate values."""
    inverted = {}
    for key, value in d.items():
        if value in inverted:
            if isinstance(inverted[value], list):
                inverted[value].append(key)
            else:
                inverted[value] = [inverted[value], key]
        else:
            inverted[value] = key
    return inverted


# ── Tests ──
if __name__ == "__main__":
    assert invert_dict({"a": 1, "b": 2}) == {1: "a", 2: "b"}
    assert invert_dict({"a": 1, "b": 1}) == {1: ["a", "b"]}
    assert invert_dict({}) == {}
    print(f"All tests passed for: Invert Dictionary")
