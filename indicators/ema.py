"""Module counts Ema indicator using mathematical formula"""

import queue
from collections import deque

class EmaCalculcator:
    """Class providing "calculate_simple_average", "calculate_ema",
    "recalculate", "get_ema" methods for counting Ema"""
    def __init__(self, period):
        """Initialize class variables, create queue and transform it into a list"""
        self.ema = 0
        self.period = period
        self.bootstrap_queue = queue.Queue(self.period/2)
        self.bootstrap_queue = deque()

    def calculate_simple_average(self):
        """Calculate simple average"""
        self.ema = float(sum(self.bootstrap_queue)) / len(self.bootstrap_queue)

    def calculate_ema(self, price):
        """Calculate Ema"""
        alpha = (2.0 / (1 + float(self.period)))
        self.ema = round((float(price) * alpha) + self.ema * (1.0 - alpha), 2)

    def recalculate(self, price):
        """Recalculate Ema"""
        if len(self.bootstrap_queue) == self.period/2:
            self.calculate_ema(price)
        else:
            self.bootstrap_queue.append(float(price))
            self.calculate_simple_average()

    def get_ema(self):
        """Return Ema"""
        return self.ema
