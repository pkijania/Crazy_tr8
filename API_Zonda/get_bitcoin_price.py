import click, time, queue
from manage_data import Data_manager
from fetch_values import Value_fetcher
from show_info_in_terminal import Terminal
from calculate_ema import Ema_calculator

@click.command()
@click.option('--data_file', help = 'Path to datafile.')
@click.option('--break_time', default = 5, help = 'Time of a break between prices.')
def main(break_time, data_file):
    data_manager = Data_manager(data_file)
    data_manager.remove_data_file()
    queue_of_prices = queue.Queue(10)
    while True:
        value_fetcher = Value_fetcher()
        price = value_fetcher.get_price()
        date = value_fetcher.get_date()
        data_manager.append_data_file(price, date)

        outcome = Ema_calculator.create_list_of_prices(queue_of_prices, price)
        print(outcome)

        converted_outcome = Ema_calculator.convert_queue_to_list(outcome)
        print(converted_outcome)

        ema = Ema_calculator.calculate_ema(converted_outcome, 5)
        print(ema)

        terminal = Terminal(break_time, price)
        terminal.show_info()
        time.sleep(int(break_time))

if __name__ == "__main__":
    main()