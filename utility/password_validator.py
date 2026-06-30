"""
Problem: Password Strength Validator
Category: Utility
Date: 2026-06-30

Description:
    Validate password strength.
"""


def validate_password(password: str) -> dict:
    """Check password strength and return detailed results."""
    checks = {
        "min_length": len(password) >= 8,
        "has_upper": any(c.isupper() for c in password),
        "has_lower": any(c.islower() for c in password),
        "has_digit": any(c.isdigit() for c in password),
        "has_special": any(not c.isalnum() for c in password),
    }
    checks["is_strong"] = all(checks.values())
    return checks


# ── Tests ──
if __name__ == "__main__":
    result = validate_password("MyP@ssw0rd")
    assert result["is_strong"] == True
    weak = validate_password("abc")
    assert weak["is_strong"] == False
    assert weak["min_length"] == False
    print(f"All tests passed for: Password Strength Validator")
