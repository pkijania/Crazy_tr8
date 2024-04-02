# Module prints all the information regarding Bitcoin trading in a terminal

import datetime, logging

class Terminal:
    """Class providing "show_info" method for showing data in a terminal"""
    def __init__(self, break_time, price, ema_long, ema_short, macd, rsi, adx, buy, sell):
        """Initialize class variables"""
        self.break_time = break_time
        self.price = price
        self.ema_long = str(ema_long)
        self.ema_short = str(ema_short)
        self.macd = macd
        self.rsi = rsi
        self.adx = adx
        self.buy = buy
        self.sell = sell

    def show_info(self):
        """Show: current price of Bitcoin in USD, current date, 
        indicators and a decision whether to buy or sell crpytocurrency"""
        logging.basicConfig(level=logging.INFO, format='%(message)s')
        date = datetime.datetime.now().strftime('%c')
        logging.info("Price of Bitcoin for: %s is: %s USD", date, self.price)
        logging.info("\nIndicators:")
        logging.info("Ema for 26 days equals: %s", self.ema_long)
        logging.info("Ema for 12 days equals: %s", self.ema_short)
        logging.info("Macd equals: %s", self.macd)
        logging.info("Rsi equals: %s", self.rsi)
        logging.info("Adx equals: %s", self.adx)
        logging.info("Buy") if self.buy == True else logging.info("Don't buy")
        logging.info("Sell") if self.sell == True else logging.info("Don't sell")
        logging.info("\nWaiting %s seconds for next fetch.\n", str(self.break_time))
