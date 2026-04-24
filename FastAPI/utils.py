def preprocess_text(text: str):
    text = text.lower().strip()
    return text


def analyze_text_logic(text: str):
    text = preprocess_text(text)

    injuries = []
    severity_score = 0

    keywords = {
        "bleeding": 3,
        "fracture": 3,
        "broken": 3,
        "not moving": 2,
        "unconscious": 2,
        "wound": 1,
        "injured": 1
    }

    for word, score in keywords.items():
        if word in text:
            injuries.append(word)
            severity_score += score

    if severity_score >= 5:
        severity = "critical"
    elif severity_score >= 3:
        severity = "high"
    elif severity_score >= 2:
        severity = "medium"
    else:
        severity = "low"

    return {
        "injury_detected": injuries if injuries else ["unknown"],
        "severity": severity
    }