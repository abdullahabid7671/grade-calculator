# grades.py

def letter_grade(score):
    """Convert numeric score (0-100) to letter grade."""
    if score >= 90:
        return "A"
    elif score >= 80:
        return "B"
    elif score >= 70:
        return "C"
    elif score >= 60:
        return "D"
    else:
        return "F"


def class_average(scores):
    """Return average of a list of scores."""
    total = 0
    for score in scores:
        total += score   # <-- BUG (should accumulate)
    return total / len(scores)


def highest_score(scores):
    """Return highest score in list."""
    best = scores[0]   # <-- BUG (fails for all negative lists)
    for score in scores:
        if score > best:
            best = score
    return best