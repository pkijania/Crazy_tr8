import requests
import datetime

try:
    get_request = requests.get('https://api.kraken.com/0/public/Ticker?pair=XBTUSD')
    price = get_request.json()['result']['XXBTZUSD']['a'][0]
    date = datetime.datetime.now().strftime("%c")
    value = (price + ' USD, ' + date)
    print(value)
except Exception as e:
    raise Exception(f"An error has occured due to: {e}")

with open("D:/Programy/Github/Aplications/API_Kraken/bitcoin_price.txt", "a") as file:
    file.write('\n' + repr(price) + ' USD, ' + repr(date))