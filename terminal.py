import datetime, logging

class Terminal:
    def __init__(self, break_time, price, ema_long, ema_short, macd, rsi, adx, buy, sell):
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
        logging.basicConfig(level=logging.INFO, format='%(message)s')
        date = datetime.datetime.now().strftime('%c')
        logging.info(f"Price of Bitcoin for: {date} is: {self.price} USD")
        logging.info(f"\nIndicators:")
        logging.info(f"Ema for 26 days equals: {self.ema_long}")
        logging.info(f"Ema for 12 days equals: {self.ema_short}")
        logging.info(f"Macd equals: {self.macd}")
        logging.info(f"Rsi equals: {self.rsi}")
        logging.info(f"Adx equals: {self.adx}")
        logging.info("Buy") if self.buy == True else logging.info("Don't buy")
        logging.info("Sell") if self.sell == True else logging.info("Don't sell")
        logging.info(f"\nWaiting {str(self.break_time)} seconds for next fetch.\n")