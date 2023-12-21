import requests
import datetime
import click
import time

@click.command()
@click.option('--data_file', help = 'Path to datafile.')
@click.option('--break_time', help = 'Time of a break between prices.')
def get_price(data_file, break_time):
    with open(data_file, 'a') as file:
        file.seek(0)
        file.truncate()
        file.write("Bitcoin prices for: " + datetime.datetime.now().strftime('%x'))
    while True:
        try:
            get_request = requests.get('https://api.kraken.com/0/public/Ticker?pair=XBTUSD')
            price = get_request.json()['result']['XXBTZUSD']['a'][0]
            date = datetime.datetime.now().strftime('%c')
            print("Bitcoin price for: " + date + " is: ")
            print(price + ' USD ')
            print("Waiting " + break_time + " seconds for next fetch.\n")
        except Exception as e:
            raise Exception(f'An error has occured due to: {e}')
        with open(data_file, 'a') as file:
            file.write('\n' + repr(price) + ' USD, ' + repr(date))
        if break_time is None:
            time.sleep(int(5))
        else:
            time.sleep(int(break_time))

if __name__ == '__main__':
    get_price()