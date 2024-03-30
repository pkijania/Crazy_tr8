from data.abstract import DataManager
import csv

class CsvFile(DataManager):
    def __init__(self, data_file):
        self.data_file = data_file

    def insert(self, price, date, ema_long, ema_short, macd, rsi, adx):
        with open(self.data_file, 'a', newline= '') as file_csv:
            writer = csv.writer(file_csv, delimiter = ',')
            writer.writerow([price, date, ema_long, ema_short, macd, rsi, adx])

    def clean(self):
        clear = open(self.data_file, 'w')
        clear.truncate()
        clear.close()