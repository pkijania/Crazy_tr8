import requests, datetime, click, time, logging

logging.basicConfig(level=logging.INFO, format='%(message)s')

def get_price():
    try:
        get_request = requests.get('https://api.kraken.com/0/public/Ticker?pair=XBTUSD')
        price = get_request.json()['result']['XXBTZUSD']['a'][0]
        date = datetime.datetime.now().strftime('%c')
    except Exception as e:
        raise Exception(f'An error has occured due to: {e}')
    return price, date

def append_data_file(data_file, price, date):
    with open(data_file, 'a') as file:
        file.write('\n' + price + ' USD, ' + date)

def remove_data_file(data_file):
    with open(data_file, 'w') as file:
        file.seek(0)
        file.truncate()
        file.write("Bitcoin prices for: " + datetime.datetime.now().strftime('%x'))

@click.command()
@click.option('--data_file', help = 'Path to datafile.')
@click.option('--break_time', default = 5, help = 'Time of a break between prices.')
def main(break_time, data_file):
    remove_data_file(data_file)
    while True:
        price, date = get_price()
        append_data_file(data_file, price, date)
        logging.info(f"Price of Bitcoin for: {date}")
        logging.info(f"{price} USD")
        logging.info("Waiting " + str(break_time) + " seconds for next fetch.\n")
        time.sleep(int(break_time))

if __name__ == "__main__":
    main()