import click, time
from fetch_values import ValueFetcher
from show_info_in_terminal import Terminal
from strategy import Strategy
from indicators.calculate_ema import EmaCalculcator
from indicators.calculate_macd import MacdCalculator
from indicators.calculate_rsi import RsiCalculator
from indicators.calculate_adx import AdxCalculator
from manage_data.put_data_into_csv import CsvFile
from manage_data.put_data_into_postgres import PostgresDataBase

@click.command()
@click.option('--data_file', help = 'Path to datafile.')
@click.option('--break_time', default = 5, help = 'Time of a break between prices.')
def main(data_file, break_time):
    # Clear all data from 'bitcoin_price.csv'
    csv_file = CsvFile(data_file)
    csv_file.remove_data_file()

    postgres = PostgresDataBase()
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

        #Based on strategy define next move
        strategy = Strategy(adx, rsi)
        strategy.order()
        buy, sell = strategy.get_order()

        # Put all the information in a 'bitcoin_price.csv' file
        csv_file.append_data_file(price, date, ema_long, ema_short, macd, rsi, adx)

        # Put all the information in a postgres data base
        postgres.transfer_data(price, date, ema_long, ema_short, macd, rsi, adx)

        # Show all the information in a terminal
        terminal = Terminal(break_time, price, ema_long, ema_short, macd, rsi, adx, buy, sell)
        terminal.show_info()
        
        # Wait 'n' seconds
        time.sleep(int(break_time))

if __name__ == "__main__":
    try:
        main()
    except Exception as error:
        print(f"Error!!, program shut down due to {error}")