"""
Problem: Deep Merge Dictionaries
Category: Dicts
Date: 2026-06-16

Description:
    Merge two dictionaries, combining nested dicts.
"""


def merge_dicts(d1: dict, d2: dict) -> dict:
    """Deep merge two dictionaries."""
    result = d1.copy()
    for key, value in d2.items():
        if key in result and isinstance(result[key], dict) and isinstance(value, dict):
            result[key] = merge_dicts(result[key], value)
        else:
            result[key] = value
    return result


# ── Tests ──
if __name__ == "__main__":
    assert merge_dicts({"a": 1}, {"b": 2}) == {"a": 1, "b": 2}
    assert merge_dicts({"a": 1}, {"a": 2}) == {"a": 2}
    assert merge_dicts({"a": {"x": 1}}, {"a": {"y": 2}}) == {"a": {"x": 1, "y": 2}}
    assert merge_dicts({}, {"a": 1}) == {"a": 1}
    print(f"All tests passed for: Deep Merge Dictionaries")
