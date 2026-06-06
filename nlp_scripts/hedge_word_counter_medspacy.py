import medspacy
from medspacy.context import ConTextRule

_HEDGE_RULES = [
    ConTextRule("suggests", "UNCERTAIN", direction="FORWARD"),
    ConTextRule("appears", "UNCERTAIN", direction="FORWARD"),
    ConTextRule("likely", "UNCERTAIN", direction="BIDIRECTIONAL"),
    ConTextRule("possible", "UNCERTAIN", direction="BIDIRECTIONAL"),
    ConTextRule("possibly", "UNCERTAIN", direction="BIDIRECTIONAL"),
    ConTextRule("may", "UNCERTAIN", direction="FORWARD"),
    ConTextRule("might", "UNCERTAIN", direction="FORWARD"),
    ConTextRule("could", "UNCERTAIN", direction="FORWARD"),
    ConTextRule("seems", "UNCERTAIN", direction="FORWARD"),
    ConTextRule("cannot exclude", "UNCERTAIN", direction="FORWARD"),
    ConTextRule("suggestive of", "UNCERTAIN", direction="FORWARD"),
    ConTextRule("questionable", "UNCERTAIN", direction="BIDIRECTIONAL"),
]

_nlp = None

def _get_nlp():
    global _nlp
    if _nlp is None:
        _nlp = medspacy.load(enable=["sentencizer", "context"])
        _nlp.get_pipe("medspacy_context").add(_HEDGE_RULES)
    return _nlp

def count_hedge_words(text):
    doc = _get_nlp()(text)
    return sum(1 for m in doc._.context_graph.modifiers if m.category == "UNCERTAIN")

# Standard interface for pattern analysis: score(text) -> float
score = count_hedge_words
