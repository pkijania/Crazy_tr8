import requests

class Value_fetcher:
    def get_price():
        try:
            get_request = requests.get('https://api.zondacrypto.exchange/rest/trading/ticker/BTC-PLN')
            price = get_request.json()['ticker']['rate']
        except Exception as e:
            raise Exception(f'An error has occured due to: {e}')
        return price

    def get_date():
        try:
            get_request = requests.get('https://api.zondacrypto.exchange/rest/trading/ticker/BTC-PLN')
            date = get_request.json()['ticker']['time']
        except Exception as e:
            raise Exception(f'An error has occured due to: {e}')
        return date