"""
Problem: Temperature Converter
Category: Utility
Date: 2026-06-08

Description:
    Convert between Celsius, Fahrenheit, and Kelvin.
"""


def celsius_to_fahrenheit(c: float) -> float:
    """Convert Celsius to Fahrenheit."""
    return round(c * 9/5 + 32, 2)

def fahrenheit_to_celsius(f: float) -> float:
    """Convert Fahrenheit to Celsius."""
    return round((f - 32) * 5/9, 2)

def celsius_to_kelvin(c: float) -> float:
    """Convert Celsius to Kelvin."""
    return round(c + 273.15, 2)


# ── Tests ──
if __name__ == "__main__":
    assert celsius_to_fahrenheit(0) == 32
    assert celsius_to_fahrenheit(100) == 212
    assert fahrenheit_to_celsius(32) == 0
    assert celsius_to_kelvin(0) == 273.15
    print(f"All tests passed for: Temperature Converter")
