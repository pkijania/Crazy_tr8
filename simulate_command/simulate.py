import click
from terminal import Terminal
from strategy import Strategy
from values.fetch_historical_values import HistoricalValueFetcher
from indicators.ema import EmaCalculcator
from indicators.macd import MacdCalculator
from indicators.rsi import RsiCalculator
from indicators.adx import AdxCalculator
from historical_data.postgres_historical_record import PostgresHitsoricalDataBase

@click.command()
@click.option('--data_source', help = '''Data source for persisting data.
        Can be either path to csv or connection string to postgres database.''')
def simulate(data_source):
    """Display the current version."""
    datamanager = PostgresHitsoricalDataBase(data_source)
    datamanager.clean()

    id_value = 0
    ema_calculator_long_period = EmaCalculcator(26)
    ema_calculator_short_period = EmaCalculcator(12)
    rsi_calculator = RsiCalculator()
    adx_calculator = AdxCalculator()
    while True:
        id_value = id_value + 1
        value_fetcher = HistoricalValueFetcher(id_value)
        price = value_fetcher.get_historical_price()
        date = value_fetcher.get_historical_date()

        #Calculate ema
        ema_calculator_long_period.recalculate(price)
        ema_calculator_short_period.recalculate(price)
        ema_long = ema_calculator_long_period.get_ema()
        ema_short = ema_calculator_short_period.get_ema()

        #Calculate macd
        macd_calcutator = MacdCalculator(ema_long, ema_short)
        macd_calcutator.calculate_macd()
        macd = macd_calcutator.get_macd()

        #Calculate rsi
        rsi_calculator.recalculate_rsi(price)
        rsi = rsi_calculator.get_rsi()

        #Calculate adx
        adx_calculator.launch(price)
        adx = adx_calculator.get_adx()

        #Based on strategy define next move
        strategy = Strategy(adx, rsi)
        strategy.order()
        buy, sell = strategy.get_order()

        #Put all the information to a specified file
        datamanager.insert(id_value, price, date, ema_long, ema_short, macd, rsi, adx)

        #Show all the information in a terminal
        terminal = Terminal(0, price, ema_long, ema_short, macd, rsi, adx, buy, sell)
        terminal.time_and_date()
        terminal.indicators()
        terminal.decision()
