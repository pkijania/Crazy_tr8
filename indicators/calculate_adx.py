import queue
from collections import deque
from indicators.calculate_ema import EmaCalculcator

class AdxCalculator:
    def __init__(self):
        self.adx = 0
        self.count = 1
        self.positive_di = self.negative_di = 0
        self.current_period_queue = queue.Queue(7)
        self.previous_period_queue = queue.Queue(7)
        self.current_period_queue = deque()
        self.previous_period_queue = deque()

    def max_and_min_price(self):
        self.max_previous = self.previous_period_queue[0]
        self.min_previous = self.previous_period_queue[0]
        self.max_current = self.current_period_queue[0]
        self.min_current = self.current_period_queue[0]
        for i in range(6):
            # Current period
            if self.current_period_queue[i] < self.min_current:
                self.min_current = self.current_period_queue[i]
            if self.current_period_queue[i] > self.max_current:
                self.max_current = self.current_period_queue[i]
            # Previous period
            if self.previous_period_queue[i] < self.min_previous:
                self.min_previous = self.previous_period_queue[i]
            if self.previous_period_queue[i] > self.max_previous:
                self.max_previous = self.previous_period_queue[i]

    def positive_and_negative_m(self):
        self.positive_m = float(self.max_current) - float(self.max_previous)
        self.negative_m = float(self.min_previous) - float(self.min_current)

    def positive_and_negative_dm(self):
        if self.positive_m > self.negative_m and self.positive_m > 0:
            self.positive_dm = self.positive_m
        else:
            self.positive_dm = 0
        if self.negative_m > self.positive_m and self.negative_m > 0:
            self.negative_dm = self.negative_m
        else:
            self.negative_dm = 0

    def tr(self):
        self.tr_value = max(float(self.max_current), float(self.previous_period_queue[6])) - min(float(self.min_current), float(self.previous_period_queue[6]))
    
    def positive_and_negative_di(self):
        if self.tr_value != 0:
            # Positive di
            self.divide_positive = self.positive_dm / self.tr_value
            self.ema_positive = EmaCalculcator(7)
            self.ema_positive.recalculate(self.divide_positive)
            self.positive_di = self.ema_positive.get_ema()
            # Negative di
            self.divide_negative = self.negative_dm / self.tr_value
            self.ema_negative = EmaCalculcator(7)
            self.ema_negative.recalculate(self.divide_negative)
            self.negative_di = self.ema_negative.get_ema()
    
    def calculate_adx(self):
        if self.positive_di + self.negative_di != 0:
            self.count_di = abs(self.positive_di - self.negative_di) / abs(self.positive_di + self.negative_di)
            self.ema = EmaCalculcator(7)
            self.ema.recalculate(self.count_di)
            self.ema_value = self.ema.get_ema()
            self.adx = round(100 * self.ema_value, 2)
    
    def launch(self, price):
        if self.count <= 7:
            self.previous_period_queue.append(price)
        elif self.count > 7 and self.count <= 14:
            self.current_period_queue.append(price)
        elif self.count > 14:
            self.max_and_min_price()
            self.positive_and_negative_m()
            self.positive_and_negative_dm()
            self.tr()
            self.positive_and_negative_di()
            self.calculate_adx()
        self.count += 1

    def get_adx(self):
        return self.adx