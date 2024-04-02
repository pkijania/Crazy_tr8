# Abstract module representing a manager of data that is erased from or insterted into a file 

from abc import ABC, abstractmethod

class DataManager(ABC):
    """Class contains "insert" and "clean" methods for managing data"""

    @abstractmethod
    def insert(self, model):
        """Method inserting data from a file"""
        pass

    @abstractmethod
    def clean(self):
        """Method erasing data from a file"""
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
        """Get method for price attribute"""
        return self.price

    @property
    def date(self):
        """Get method for date attribute"""
        return self.date

    @property
    def ema_long(self):
        """Get method for long term ema indicator attribute"""
        return self.ema_long

    @property
    def ema_short(self):
        """Get method for short term ema indicator attribute"""
        return self.ema_short

    @property
    def macd(self):
        """Get method for macd indicator attribute"""
        return self.macd

    @property
    def rsi(self):
        """Get method for rsi indicator attribute"""
        return self.rsi

    @property
    def adx(self):
        """Get method for adx indicator attribute"""
        return self.adx
