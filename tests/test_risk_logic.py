"""Small tests for the illustrative rule-based demo logic."""

def assess(angle, velocity, confidence, low=10, high=90, margin=10):
    if confidence < 50:
        return "CHECK SENSOR"
    if angle < low or angle > high:
        return "OUTSIDE DEMO RANGE"
    if min(angle - low, high - angle) <= margin or velocity >= 150:
        return "CAUTION"
    return "WITHIN DEMO RANGE"


def test_within_range():
    assert assess(55, 35, 95) == "WITHIN DEMO RANGE"


def test_near_limit():
    assert assess(88, 30, 95) == "CAUTION"


def test_outside_range():
    assert assess(110, 40, 95) == "OUTSIDE DEMO RANGE"


def test_fast_motion():
    assert assess(45, 180, 95) == "CAUTION"


def test_low_confidence():
    assert assess(50, 30, 20) == "CHECK SENSOR"
