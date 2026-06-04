def estimate_pi_risk(text):
    # Mock PI (Protected Information) risk estimator.
    # Replace with a proper NER-based implementation in production.
    risk_score = 0
    if "patient identifier" in text.lower() or "social security number" in text.lower():
        risk_score = 10
    elif "patient name" in text.lower() or "date of birth" in text.lower():
        risk_score = 5
    return risk_score

# Standard interface for pattern analysis: score(text) -> float
score = estimate_pi_risk
