import requests
import datetime

get_request = requests.get('https://api.kraken.com/0/public/Ticker?pair=XBTUSD')
price = get_request.json()['result']['XXBTZUSD']['a'][0]
date = datetime.datetime.now().strftime("%c")
try:
    print("Price of bitcon for:", date, "is", price)
except:
    print("An error has occured")