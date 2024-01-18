import click, time
from manage_data import DataManager
from fetch_values import ValueFetcher
from show_info_in_terminal import Terminal
from calculate_ema import EmaCalculcator
from calculate_macd import MacdCalculator
from calculate_rsi import RsiCalculator
from calculate_adx import AdxCalculator

@click.command()
@click.option('--data_file', help = 'Path to datafile.')
@click.option('--break_time', default = 5, help = 'Time of a break between prices.')
def main(data_file, break_time):
    # Clear all data from 'bitcoin_price.csv'
    data_manager = DataManager(data_file)
    data_manager.remove_data_file()

    ema_calculator_long_period = EmaCalculcator(26)
    ema_calculator_short_period = EmaCalculcator(12)
    rsi_calculator = RsiCalculator()
    adx_calculator = AdxCalculator()
    while True:
        # Fetch current Bitcoin price and unix time from 'zondacrypto'
        value_fetcher = ValueFetcher()
        price = value_fetcher.get_price()
        date = value_fetcher.get_date()

        # Calculate ema
        ema_calculator_long_period.recalculate(price)
        ema_calculator_short_period.recalculate(price)
        ema_long = ema_calculator_long_period.get_ema()
        ema_short = ema_calculator_short_period.get_ema()

        # Calculate macd
        macd_calcutator = MacdCalculator(ema_long, ema_short)
        macd_calcutator.calculate_macd()
        macd = macd_calcutator.get_macd()

        # Calculate rsi
        rsi_calculator.recalculate_rsi(price)
        rsi = rsi_calculator.get_rsi()

        #Calculate adx
        adx_calculator.launch(price)
        adx = adx_calculator.get_adx()

        # Put all the information in a 'bitcoin_price.csv' file
        data_manager.append_data_file(price, date, ema_long, ema_short, macd, rsi, adx)

        # Show all the information in a terminal
        terminal = Terminal(break_time, price, ema_long, ema_short, macd, rsi, adx)
        terminal.show_info()

        # Wait 'n' seconds
        time.sleep(int(break_time))

if __name__ == "__main__":
    main()