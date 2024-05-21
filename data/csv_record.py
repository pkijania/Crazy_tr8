"""Module deletes old data and adds new data to a csv_record.py file"""

from data.abstract import DataManager
import csv

class CsvFile(DataManager):
    """Class providing "insert" and "clean" methods for managing data in a "csv_record.py" file"""
    def __init__(self, data_file):
        """Initialize class variable"""
        self.data_file = data_file

    def insert(self, id_value, price, date, ema_long, ema_short, macd, rsi, adx):
        """Insert data into a "csv_record.py" file"""
        with open(self.data_file, 'a', newline= '') as file_csv:
            writer = csv.writer(file_csv, delimiter = ',')
            writer.writerow([id_value, price, date, ema_long, ema_short, macd, rsi, adx])

    def clean(self):
        """Erase data into a "csv_record.py" file"""
        clear = open(self.data_file, 'w')
        clear.truncate()
        clear.close()
