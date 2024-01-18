class MacdCalculator:
    def __init__(self, ema_long, ema_short):
        self.ema_long = ema_long
        self.ema_short = ema_short
    
    def calculate_macd(self):
        self.macd = round(self.ema_short - self.ema_long, 2)
    
    def get_macd(self):
        return self.macd