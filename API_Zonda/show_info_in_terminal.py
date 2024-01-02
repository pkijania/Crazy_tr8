import datetime, logging

class Terminal:
    def __init__(self, break_time, price, ema):
        self.break_time = break_time
        self.price = price
        self.ema = ema

    def show_info(self):
        logging.basicConfig(level=logging.INFO, format='%(message)s')
        date = datetime.datetime.now().strftime('%c')
        logging.info(f"Price of Bitcoin for: {date} is: {self.price} USD")
        logging.info("Ema equals: " + self.ema)
        logging.info("Waiting " + str(self.break_time) + " seconds for next fetch.\n")