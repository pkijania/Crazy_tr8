import click, time, queue
from manage_data import Data_manager
from fetch_values import Value_fetcher
from show_info_in_terminal import Terminal
from calculate_ema import Ema_calculator

@click.command()
@click.option('--data_file', help = 'Path to datafile.')
@click.option('--break_time', default = 5, help = 'Time of a break between prices.')
def main(break_time, data_file):
    # Clear all data from 'bitcoin_price.csv' and creat a queue
    data_manager = Data_manager(data_file)
    data_manager.remove_data_file()
    queue_of_prices = queue.Queue(10)

    while True:
        # Fetch current Bitcoin price and unix time and put it in 'bitcoin_price.csv'
        value_fetcher = Value_fetcher()
        price = value_fetcher.get_price()
        date = value_fetcher.get_date()
        data_manager.append_data_file(price, date)

        # Put current Bitcoin price in a queue, convert it to a list and count ema
        outcome = Ema_calculator.create_queue_of_prices(queue_of_prices, price)
        converted_outcome = Ema_calculator.convert_queue_to_list(outcome)
        ema = Ema_calculator.calculate_ema(converted_outcome, 5)

        # Show all the information in a terminal
        terminal = Terminal(break_time, price, ema)
        terminal.show_info()

        # Wait 'n' seconds
        time.sleep(int(break_time))

if __name__ == "__main__":
    main()