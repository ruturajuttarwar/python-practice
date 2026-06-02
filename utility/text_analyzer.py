"""
Problem: Text Analyzer
Category: Utility
Date: 2026-06-02

Description:
    Count total words, unique words, and most common word in a text.
"""


def analyze_text(text: str) -> dict:
    """Analyze text and return word statistics."""
    words = text.lower().split()
    freq = {}
    for w in words:
        cleaned = ''.join(c for c in w if c.isalnum())
        if cleaned:
            freq[cleaned] = freq.get(cleaned, 0) + 1
    most_common = max(freq, key=freq.get) if freq else None
    return {
        "total_words": len(words),
        "unique_words": len(freq),
        "most_common": most_common,
        "frequencies": freq,
    }


# ── Tests ──
if __name__ == "__main__":
    result = analyze_text("the cat sat on the mat")
    assert result["total_words"] == 6
    assert result["unique_words"] == 5
    assert result["most_common"] == "the"
    print(f"All tests passed for: Text Analyzer")
