import pytest

def calculate_ema(prices, days):
    ema = [sum(prices[:days]) / days]
    for price in prices[days:]:
        ema.append((price * (2 / (1 + days))) + ema[-1] * (1 - (2 / (1 + days))))
    return ema

prices = [100, 105, 110, 115, 120, 125, 130, 135, 140, 145]
period = 5

ema = calculate_ema(prices, period)
assert ema == [110.0, 115.0, 120.0, 125.00000000000001, 130.00000000000003, 135.00000000000003], "Assertion failed"
print (ema)