import requests

class Value_fetcher:
    def __init__(self):
        get_request = requests.get('https://api.zondacrypto.exchange/rest/trading/ticker/BTC-PLN')
        self.get_request = get_request
        
    def get_price(self):
        try:
            return self.get_request.json()['ticker']['rate']
        except Exception as e:
            raise Exception(f'An error has occured due to: {e}')

    def get_date(self):
        try:
            return self.get_request.json()['ticker']['time']
        except Exception as e:
            raise Exception(f'An error has occured due to: {e}')