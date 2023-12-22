import requests
import datetime
import click
import time

@click.command()
@click.option('--data_file', help = 'Path to datafile.')
@click.option('--break_time', default = 5, help = 'Time of a break between prices.')

def get_price():
    try:
        get_request = requests.get('https://api.kraken.com/0/public/Ticker?pair=XBTUSD')
        price = get_request.json()['result']['XXBTZUSD']['a'][0]
        date = datetime.datetime.now().strftime('%c')
    except Exception as e:
        raise Exception(f'An error has occured due to: {e}')
    return price, date

def append_data_file(data_file, get_price):
    with open(data_file, 'a') as file:
        file.write('\n' + get_price)

def remove_data_file(data_file):
    with open(data_file, 'a') as file:
        file.seek(0)
        file.truncate()
        file.write("Bitcoin prices for: " + datetime.datetime.now().strftime('%x'))

def main(break_time, data_file):
    remove_data_file(data_file)
    while True:
        print(get_price())
        append_data_file(data_file)
        print("Waiting " + str(break_time) + " seconds for next fetch.\n")
        time.sleep(int(break_time))