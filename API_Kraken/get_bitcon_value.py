import requests

get_request = requests.get('https://api.kraken.com/0/public/Ticker?pair=XBTUSD')
if get_request is None:
    raise Exception(f"An error has occurred")
print("Status code is:", get_request)
print(get_request.json())