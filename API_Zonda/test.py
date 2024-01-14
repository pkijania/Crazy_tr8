import pytest, math
from calculate_ema import EmaCalculcator
from calculate_macd import MacdCalculator
from calculate_rsi import RsiCalculator

def test_ema():
    prices = [100, 105, 110, 115, 120, 125, 130, 135, 140, 145]
    ema_test = EmaCalculcator(2)
    for price in prices: 
        ema_test.recalculate(price)
    ema = ema_test.get_ema()
    assert math.fabs(ema - 142.5) < 0.01, "Assertion failed"

def test_macd():
    prices = [100, 105, 110, 115, 120, 125, 130, 135, 140, 145]
    ema_test_long = EmaCalculcator(4)    
    ema_test_short = EmaCalculcator(2)
    for price in prices: 
        ema_test_long.recalculate(price)
        ema_test_short.recalculate(price)
    ema_long = ema_test_long.get_ema()
    ema_short = ema_test_short.get_ema()
    macd_test = MacdCalculator(ema_long, ema_short)
    macd_test.calculate_macd()
    macd = macd_test.get_macd()
    assert math.fabs(macd - 5) < 0.1, "Assertion failed"

def test_rsi():
    prices = [100, 105, 100, 115, 100, 125, 100, 135, 140, 145, 100, 120, 100, 140, 120]
    rsi_test = RsiCalculator()
    for price in prices: 
        rsi_test.recalculate_rsi(price)
    rsi = rsi_test.get_rsi()
    assert math.fabs(rsi - 50) < 0.01, "Assertion failed"