from abc import ABC, abstractmethod

class DataManager(ABC):

    @abstractmethod
    def insert(self, model):
        pass

    @abstractmethod
    def clean(self):
        pass

class Model:
    @property
    def __init__(self, price, date, ema_long, ema_short, macd, rsi, adx):
        self.price = price
        self.date = date
        self.ema_long = ema_long
        self.ema_short = ema_short
        self.macd = macd
        self.rsi = rsi
        self.adx = adx

    @property
    def price(self):
        return self.price

    @property
    def date(self):
        return self.date

    @property
    def ema_long(self):
        return self.ema_long

    @property
    def ema_short(self):
        return self.ema_short

    @property
    def macd(self):
        return self.macd

    @property
    def rsi(self):
        return self.rsi

    @property
    def adx(self):
        return self.adx
