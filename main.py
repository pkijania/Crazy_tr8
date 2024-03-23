import click, time
from fetch_values import ValueFetcher
from terminal import Terminal
from strategy import Strategy
from indicators.ema import EmaCalculcator
from indicators.macd import MacdCalculator
from indicators.rsi import RsiCalculator
from indicators.adx import AdxCalculator
from data.csv import CsvFile
from data.postgres import PostgresDataBase

@click.command()
@click.option('--data_source', help = 'Data source for persisting data. Can be either path to csv or connection string to postgres database.')
@click.option('--break_time', default = 5, help = 'Time of a break between prices.')
def main(data_source, break_time):
    if data_source.startswith("postgresql://"):
        datamanager = PostgresDataBase()
    else:
        datamanager = CsvFile(data_source)
    
    # Clean all data from a specified file
    datamanager.clean()
    
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
            
        # Put all the information to a specified file
        datamanager.insert(price, date, ema_long, ema_short, macd, rsi, adx)

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