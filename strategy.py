class Strategy:
    def __init__(self, adx, rsi):
        self.adx = adx
        self.rsi = rsi
        self.adx_threshold = 30
        self.rsi_upper_threshold = 70
        self.rsi_lower_threshold = 30
        self.buy = False
        self.sell = False

    def order(self):
        if self.adx > self.adx_threshold and self.rsi < self.rsi_lower_threshold:
            self.buy = True
        elif self.adx > self.adx_threshold and self.rsi > self.rsi_upper_threshold:
            self.sell = True

    def get_order(self):
        return self.buy, self.sell
