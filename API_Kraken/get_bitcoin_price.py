import requests
import datetime
import click
import time

@click.command()
@click.option('--data_file', help = 'Path to datafile.')
def get_price(data_file):
    with open(data_file, 'a') as file:
        file.seek(0)
        file.truncate()
        file.write("Bitcoin prices for: " + datetime.datetime.now().strftime('%x'))
    while True:
        try:
            get_request = requests.get('https://api.kraken.com/0/public/Ticker?pair=XBTUSD')
            price = get_request.json()['result']['XXBTZUSD']['a'][0]
            date = datetime.datetime.now().strftime('%c')
            value = (price + ' USD ')
            print("Bitcoin price for: " + date + " is: ")
            print(value)
            print("Waiting 5 seconds for next fetch.\n")
        except Exception as e:
            raise Exception(f'An error has occured due to: {e}')
        with open(data_file, 'a') as file:
            file.write('\n' + repr(price) + ' USD, ' + repr(date))
        time.sleep(5)

if __name__ == '__main__':
    get_price()