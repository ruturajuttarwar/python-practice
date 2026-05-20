"""
Problem: Group By Key
Category: Dicts
Date: 2026-05-20

Description:
    Group a list of dictionaries by a given key.
"""


def group_by(items: list, key: str) -> dict:
    """Group list of dicts by a given key."""
    groups = {}
    for item in items:
        k = item.get(key)
        if k not in groups:
            groups[k] = []
        groups[k].append(item)
    return groups


# ── Tests ──
if __name__ == "__main__":
    data = [{"name": "Alice", "dept": "Eng"}, {"name": "Bob", "dept": "Eng"}, {"name": "Carol", "dept": "HR"}]
    result = group_by(data, "dept")
    assert len(result["Eng"]) == 2
    assert len(result["HR"]) == 1
    print(f"All tests passed for: Group By Key")
