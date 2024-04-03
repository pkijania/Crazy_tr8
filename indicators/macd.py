"""Module counts Macd indicator using mathematical formula"""

class MacdCalculator:
    """Class providing "calculate_macd" and "get_macd" methods for Macd counting"""
    def __init__(self, ema_long, ema_short):
        """Initialize class variables"""
        self.ema_long = ema_long
        self.ema_short = ema_short
        self.macd = 0

    def calculate_macd(self):
        """Calculate Macd"""
        self.macd = round(self.ema_short - self.ema_long, 2)

    def get_macd(self):
        """Return Macd"""
        return self.macd
