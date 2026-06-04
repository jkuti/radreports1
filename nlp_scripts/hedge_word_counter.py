import re

def count_hedge_words(text):
    hedge_words = ["suggests", "appears", "likely", "possible", "may", "might", "could", "indicates", "seems"]
    count = 0
    for word in hedge_words:
        count += len(re.findall(r"\b" + word + r"\b", text.lower()))
    return count

# Standard interface for pattern analysis: score(text) -> float
score = count_hedge_words
