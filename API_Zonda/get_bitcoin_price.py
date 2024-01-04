import click, time
from manage_data import DataManager
from fetch_values import ValueFetcher
from show_info_in_terminal import Terminal
from calculate_ema import EmaCalculcator

@click.command()
@click.option('--data_file', help = 'Path to datafile.')
@click.option('--break_time', default = 5, help = 'Time of a break between prices.')
def main(break_time, data_file):
    # Clear all data from 'bitcoin_price.csv'
    data_manager = DataManager(data_file)
    data_manager.remove_data_file()
    ema_calculator = EmaCalculcator(26)
    while True:
        # Fetch current Bitcoin price and unix time from 'zondacrypto' and put it in a 'bitcoin_price.csv' file
        value_fetcher = ValueFetcher()
        price = value_fetcher.get_price()
        date = value_fetcher.get_date()
        data_manager.append_data_file(price, date)

        # Calculate ema
        ema_calculator.recalculate(price)
        ema = ema_calculator.get_ema()

        # Show all the information in a terminal
        terminal = Terminal(break_time, price, ema)
        terminal.show_info()

        # Wait 'n' seconds
        time.sleep(int(break_time))

if __name__ == "__main__":
    main()