import pytest, math
from calculate_ema import EmaCalculcator

@pytest.fixture()
def test_ema():
    prices = [100, 105, 110, 115, 120, 125, 130, 135, 140, 145]
    ema_test = EmaCalculcator(26)
    for price in prices: 
        ema_test.recalculate(price)
    ema = ema_test.get_ema()
    assert math.fabs(ema - 130.487) < 0.01, "Assertion failed"