import requests, datetime, click, time, logging
from manage_data import Data_manager

logging.basicConfig(level=logging.INFO, format='%(message)s')

def get_price():
    try:
        get_request = requests.get('https://api.kraken.com/0/public/Ticker?pair=XBTUSD')
        price = get_request.json()['result']['XXBTZUSD']['a'][0]
    except Exception as e:
        raise Exception(f'An error has occured due to: {e}')
    return price

@click.command()
@click.option('--data_file', help = 'Path to datafile.')
@click.option('--break_time', default = 5, help = 'Time of a break between prices.')
def main(break_time, data_file):
    Data_manager.remove_data_file(data_file)
    while True:
        price = get_price()
        date = datetime.datetime.now().strftime('%c')
        Data_manager.append_data_file(data_file, price, date)
        logging.info(f"Price of Bitcoin for: {date}")
        logging.info(f"{price}")
        logging.info("Waiting " + str(break_time) + " seconds for next fetch.\n")
        time.sleep(int(break_time))

if __name__ == "__main__":
    main()