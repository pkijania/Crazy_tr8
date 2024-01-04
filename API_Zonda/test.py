import pytest, math

@pytest.fixture()
def test_ema(ema):
    assert math.fabs(ema - 172500) < 0.01, "Assertion failed"