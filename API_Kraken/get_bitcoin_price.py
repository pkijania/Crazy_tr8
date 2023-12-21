import requests
import datetime
import click

@click.command()
@click.option('--data_file', help = 'Path to datafile.')
def get_price(data_file):
    try:
        get_request = requests.get('https://api.kraken.com/0/public/Ticker?pair=XBTUSD')
        price = get_request.json()['result']['XXBTZUSD']['a'][0]
        date = datetime.datetime.now().strftime('%c')
        value = (price + ' USD, ' + date)
        print(value)
    except Exception as e:
        raise Exception(f'An error has occured due to: {e}')
    with open(data_file, 'a') as file:
        file.write('\n' + repr(price) + ' USD, ' + repr(date))

if __name__ == '__main__':
    get_price()