import datetime, click, time, logging
from manage_data import Data_manager
from fetch_values import Value_fetcher

def show_info(break_time, price):
    logging.basicConfig(level=logging.INFO, format='%(message)s')
    date = datetime.datetime.now().strftime('%c')
    logging.info(f"Price of Bitcoin for: {date}")
    logging.info(f"{price}")
    logging.info("Waiting " + str(break_time) + " seconds for next fetch.\n")

@click.command()
@click.option('--data_file', help = 'Path to datafile.')
@click.option('--break_time', default = 5, help = 'Time of a break between prices.')
def main(break_time, data_file):
    data_manager = Data_manager(data_file)
    value_fetcher = Value_fetcher()
    data_manager.remove_data_file()
    while True:
        price = value_fetcher.get_price()
        date = value_fetcher.get_date()
        data_manager.append_data_file(price, date)
        show_info(break_time, price)
        time.sleep(int(break_time))

if __name__ == "__main__":
    main()