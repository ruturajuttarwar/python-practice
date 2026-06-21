"""
Problem: Valid Parentheses
Category: Utility
Date: 2026-06-21

Description:
    Check if a string of parentheses is valid.
"""


def is_valid_parentheses(s: str) -> bool:
    """Check if parentheses string is valid."""
    stack = []
    mapping = {')': '(', ']': '[', '}': '{'}
    for char in s:
        if char in mapping.values():
            stack.append(char)
        elif char in mapping:
            if not stack or stack[-1] != mapping[char]:
                return False
            stack.pop()
    return len(stack) == 0


# ── Tests ──
if __name__ == "__main__":
    assert is_valid_parentheses("()[]{}") == True
    assert is_valid_parentheses("(]") == False
    assert is_valid_parentheses("([)]") == False
    assert is_valid_parentheses("{[]}") == True
    assert is_valid_parentheses("") == True
    print(f"All tests passed for: Valid Parentheses")
