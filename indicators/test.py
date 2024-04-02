# Module tests correctness of all indicators modules

import pytest, math
from indicators.ema import EmaCalculcator
from indicators.macd import MacdCalculator
from indicators.rsi import RsiCalculator
from indicators.adx import AdxCalculator

def test_ema():
    """Test correctness of Ema module"""
    prices = [100, 105, 110, 115, 120, 125, 130, 135, 140, 145]
    ema_test = EmaCalculcator(2)
    for price in prices: 
        ema_test.recalculate(price)
    ema = ema_test.get_ema()
    assert math.fabs(ema - 142.5) < 0.01, "Assertion failed"

def test_macd():
    """Test correctness of Macd module"""
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
    """Test correctness of Rsi module"""
    prices = [100, 105, 100, 115, 100, 125, 100, 135, 140, 145, 100, 120, 100, 140, 120]
    rsi_test = RsiCalculator()
    for price in prices: 
        rsi_test.recalculate_rsi(price)
    rsi = rsi_test.get_rsi()
    assert math.fabs(rsi - 50) < 0.01, "Assertion failed"

def test_adx():
    """Test correctness of Adx module"""
    prices = [100, 105, 100, 115, 100, 125, 100, 135, 140, 145, 100, 120, 100, 140, 120]
    adx_test = AdxCalculator()
    for price in prices:
        adx_test.launch(price)
    adx = adx_test.get_adx()
    assert math.fabs(adx - 100) < 0.01, "Assertion failed"
