import requests
import datetime

get_request = requests.get('https://api.kraken.com/0/public/Ticker?pair=XBTUSD')
price = get_request.json()['result']['XXBTZUSD']['a'][0]
date = datetime.datetime.now().strftime("%c")
value = ('Price of bitcon for: ' + date + ' is: ' + price + ' USD')
try:
    print(value)
except:
    print("An error has occured")

value_txt = {"Price of bitcon for:" : date, "is" : price}

file = open("bitcoin_price.txt", "w")
value_txt = repr(value_txt)
file.write(value_txt + "USD")

file.close()