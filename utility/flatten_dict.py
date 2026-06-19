"""
Problem: Flatten Dictionary
Category: Utility
Date: 2026-06-19

Description:
    Flatten a nested dictionary with dot-separated keys.
"""


def flatten_dict(d: dict, parent_key: str = '', sep: str = '.') -> dict:
    """Flatten nested dict with dot-separated keys."""
    items = {}
    for k, v in d.items():
        new_key = f"{parent_key}{sep}{k}" if parent_key else k
        if isinstance(v, dict):
            items.update(flatten_dict(v, new_key, sep))
        else:
            items[new_key] = v
    return items


# ── Tests ──
if __name__ == "__main__":
    assert flatten_dict({"a": {"b": 1, "c": 2}}) == {"a.b": 1, "a.c": 2}
    assert flatten_dict({"x": 1}) == {"x": 1}
    assert flatten_dict({}) == {}
    assert flatten_dict({"a": {"b": {"c": 3}}}) == {"a.b.c": 3}
    print(f"All tests passed for: Flatten Dictionary")
