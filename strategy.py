# Module returns a decision whether to buy or sell cryptocurrency

class Strategy:
    """Class providing "order" and "get_order" methods for decision making"""
    def __init__(self, adx, rsi):
        """Initialize class variables"""
        self.adx = adx
        self.rsi = rsi
        self.adx_threshold = 30
        self.rsi_upper_threshold = 70
        self.rsi_lower_threshold = 30
        self.buy = False
        self.sell = False

    def order(self):
        """Compare amounts of indicators and 
        assigning true value to a certain attribute"""
        if self.adx > self.adx_threshold and self.rsi < self.rsi_lower_threshold:
            self.buy = True
        elif self.adx > self.adx_threshold and self.rsi > self.rsi_upper_threshold:
            self.sell = True

    def get_order(self):
        """Return sell and buy attributes"""
        return self.buy, self.sell
