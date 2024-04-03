"""Module counts Rsi indicator using mathematical formula"""

import queue
from collections import deque

class RsiCalculator:
    """Class providing "calculate_gain_and_loss", "calculate_average_gain_and_loss",
    "calculate_rs", "calculate_rsi", "recalculate_rsi" and "get_rsi" methods for counting Rsi"""
    def __init__(self):
        """Initialize class variables, create queue and transform it into a list"""
        self.bootstrap_queue = queue.Queue(14)
        self.bootstrap_queue = deque()
        self.rs = self.rsi = self.average_gain = self.average_loss = 0
        self.gain = self.loss = []

    def calculate_gain_and_loss(self):
        """Calculate gain and loss"""
        for i in range(0, 13):
            if self.bootstrap_queue[i + 1] > self.bootstrap_queue[i]:
                self.gain.append(self.bootstrap_queue[i + 1] - self.bootstrap_queue[i])
            elif self.bootstrap_queue[i + 1] < self.bootstrap_queue[i]:
                self.loss.append(self.bootstrap_queue[i] - self.bootstrap_queue[i + 1])

    def calculate_average_gain_and_loss(self):
        """Calculate average gain and loss"""
        if len(self.gain) != 0:
            self.average_gain = sum(self.gain) / len(self.gain)
        if len(self.loss) != 0:
            self.average_loss = sum(self.loss) / len(self.loss)

    def calculate_rs(self):
        """Calculate Rs"""
        if self.average_loss != 0:
            self.rs = self.average_gain / self.average_loss

    def calculate_rsi(self):
        """Calculate Rsi"""
        if self.rs != 0:
            self.rsi = round(100 - (100 / (1 + self.rs)))

    def recalculate_rsi(self, price):
        """Recalculate Rsi"""
        if len(self.bootstrap_queue) == 14:
            self.calculate_gain_and_loss()
            self.calculate_average_gain_and_loss()
            self.calculate_rs()
            self.calculate_rsi()
        else:
            self.bootstrap_queue.append(float(price))

    def get_rsi(self):
        """Return Rsi"""
        return self.rsi
