import pytest, queue

class List_of_prices_constructor:
    def create_queue_of_prices(queue_of_prices, price):
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
            list_of_string_prices = list(queue_of_prices)
            list_of_float_prices = []
            for item in list_of_string_prices:
                list_of_float_prices.append(float(item))
            return list_of_float_prices
        except Exception as e:
            raise Exception(f'An error has occured due to: {e}')

class Ema_calculator:
    def calculate_ema(list_of_prices, days):
        start_ema = int((days - 1) / 2)
        alpha = (2.0 / (1 + float(days)))
        if len(list_of_prices) > days:
            ema = float(sum(list_of_prices[:start_ema])) / start_ema
            for price in list_of_prices[start_ema - 1:-1]:
                ema = (price * alpha) + ema * (1.0 - alpha)
            return ema
        else:
            return 0