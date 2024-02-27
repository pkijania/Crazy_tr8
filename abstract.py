from abc import ABC, abstractmethod

class DataManager(ABC):

    @abstractmethod
    def insert(self, model):
        pass
        
class Model:
    def __init__(self, price, date, ema_long, ema_short, macd, rsi, adx):
        self._price = price
        self._date = date
        self._ema_long = ema_long
        self._ema_short = ema_short
        self._macd = macd
        self._rsi = rsi
        self._adx = adx

    @property
    def price(self):
        return self._price

    @property
    def date(self):
        return self._date