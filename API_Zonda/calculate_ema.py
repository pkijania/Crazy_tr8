import pytest, queue, math
from collections import deque

class Ema_calculator:
    def create_list_of_prices(queue_of_prices, price):
        try:
            if queue_of_prices.full():
                queue_of_prices.get()
                queue_of_prices.put(price)
            else:
                queue_of_prices.put(price)
            return queue_of_prices.queue
        except Exception as e:
            raise Exception(f'An error has occured due to: {e}')
        
    def convert_queue_to_list(queue_of_prices):
        try:
            return list(queue_of_prices)
        except Exception as e:
            raise Exception(f'An error has occured due to: {e}')

    def calculate_ema(list_of_prices, days):
        alpha = (2.0 / (1 + float(days)))
        # determines at which element we start calculating ema 
        start_ema = int((days - 1) / 2)
        ema = float(sum(list_of_prices[:start_ema])) / start_ema
        for price in list_of_prices[start_ema-1:-1]:
            ema = (price * alpha) + ema * (1.0 - alpha)
        return ema

#prices = [100, 105, 110, 115, 120, 125, 130, 135, 140, 145]
#period = 5

#ema = Ema_calculator.calculate_ema(prices, period)
#assert math.fabs(ema-130.487) < 0.01, "Assertion failed"
#print(ema)
