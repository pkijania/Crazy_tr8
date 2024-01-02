import pytest, math

class Test:
    def test_check_ema(ema):
        assert math.fabs(ema - 130.487) < 0.01, "Assertion failed"