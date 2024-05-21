"""Module gets information from Zondacrypto about current price of Bitcoin and current date using
API requests"""

import requests

class ValueFetcher:
    """Class providing "get_price" and "get_date" methods for getting price and date data"""
    def __init__(self):
        """Connect to Zondacrypto API using get request and initialize class variable"""
        get_request = requests.get('https://api.zondacrypto.exchange/rest/trading/ticker/BTC-USD')
        self.get_request = get_request

    def get_price(self):
        """Get the current price of Bitcoin in USD"""
        try:
            return self.get_request.json()['ticker']['rate']
        except Exception as e:
            raise Exception(f'An error has occured due to: {e}')

    def get_date(self):
        """Get the current date in Unix Time Stamp"""
        try:
            return self.get_request.json()['ticker']['time']
        except Exception as e:
            raise Exception(f'An error has occured due to: {e}')
