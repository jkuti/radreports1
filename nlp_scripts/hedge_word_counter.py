import re

_HEDGE_WORDS = [
    "suggests", "suggest",
    "appears", "appear",
    "likely", "unlikely",
    "possible", "possibly", "possibility",
    "probable", "probably",
    "may", "might", "could",
    "seems", "seem",
    "questionable",
    "cannot exclude", "can not exclude",
    "suggestive of",
    "suspicious for", "suspicious of",
    "consistent with",
    "cannot be excluded",
    "presumed", "presumptive",
    "apparent",
    "equivocal",
    "indeterminate",
    "uncertain",
]

# Sort longest first so multi-word phrases match before their substrings
_SORTED_PHRASES = sorted(_HEDGE_WORDS, key=len, reverse=True)
_PATTERNS = [re.compile(r"\b" + re.escape(p) + r"\b", re.IGNORECASE) for p in _SORTED_PHRASES]


def count_hedge_words(text):
    matched_spans = []
    for pattern in _PATTERNS:
        for m in pattern.finditer(text):
            span = (m.start(), m.end())
            if not any(s <= span[0] and span[1] <= e for s, e in matched_spans):
                matched_spans.append(span)
    return len(matched_spans)


# Standard interface for pattern analysis: score(text) -> float
score = count_hedge_words
