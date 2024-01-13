import queue
from collections import deque

class EmaCalculcator:
    def __init__(self, period):
        self.ema = 0
        self.period = period
        self.bootstrap_queue = queue.Queue(self.period/2)
        self.bootstrap_queue = deque()
    
    def calculate_simple_average(self):
        self.ema = float(sum(self.bootstrap_queue)) / len(self.bootstrap_queue)

    def calculate_ema(self, price):
        alpha = (2.0 / (1 + float(self.period)))
        self.ema = round((float(price) * alpha) + self.ema * (1.0 - alpha), 4)
              
    def recalculate(self, price):
        if len(self.bootstrap_queue) == self.period/2:
            self.calculate_ema(price)
        else:
            self.bootstrap_queue.append(float(price))
            self.calculate_simple_average()

    def get_ema(self):
        return self.ema