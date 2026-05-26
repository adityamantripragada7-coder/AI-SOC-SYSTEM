def calculate_risk(ml_score, intel_score):

    print(f"ML Score: {ml_score}, Intel Score: {intel_score}")

    risk = (ml_score * 0.6) + (intel_score * 0.4)

    print(f"Final Risk Score: {risk}")

    return risk


def get_severity(score):

    if score > 80:
        return "CRITICAL"
    elif score > 60:
        return "HIGH"
    elif score > 30:
        return "MEDIUM"
    else:
        return "LOW"