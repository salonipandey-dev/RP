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

def predict_severity_logic(text: str, image_confidence: float):
    text = text.lower()

    score = 0

    # text scoring
    if "bleeding" in text:
        score += 3

    if "fracture" in text or "broken" in text:
        score += 3

    if "unconscious" in text or "not moving" in text:
        score += 2

    if "wound" in text:
        score += 1

    # image confidence scoring
    if image_confidence >= 0.90:
        score += 2
    elif image_confidence >= 0.75:
        score += 1

    # final priority
    if score >= 6:
        priority = "CRITICAL"
    elif score >= 4:
        priority = "HIGH"
    elif score >= 2:
        priority = "MEDIUM"
    else:
        priority = "LOW"

    return {"priority": priority, "score": score}