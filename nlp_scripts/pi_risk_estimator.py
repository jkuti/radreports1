from presidio_analyzer import AnalyzerEngine

# Higher weight = more sensitive entity type
_ENTITY_WEIGHTS = {
    "US_SSN": 10,
    "CREDIT_CARD": 8,
    "US_DRIVER_LICENSE": 8,
    "MEDICAL_LICENSE": 7,
    "US_BANK_NUMBER": 7,
    "PHONE_NUMBER": 5,
    "EMAIL_ADDRESS": 5,
    "PERSON": 4,
    "LOCATION": 3,
    "DATE_TIME": 2,
}

_analyzer = None

def _get_analyzer():
    global _analyzer
    if _analyzer is None:
        _analyzer = AnalyzerEngine()
    return _analyzer

def estimate_pi_risk(text):
    results = _get_analyzer().analyze(text=text, language="en")
    return sum(_ENTITY_WEIGHTS.get(r.entity_type, 1) for r in results)

# Standard interface for pattern analysis: score(text) -> float
score = estimate_pi_risk
