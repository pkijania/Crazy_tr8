import csv

class DataManager:
    def __init__(self, data_file):
        self.data_file = data_file

    def append_data_file(self, price, date):
        with open(self.data_file, 'a', newline= '') as file_csv:
            writer = csv.writer(file_csv, delimiter = ',')
            writer.writerow([price, date])

    def remove_data_file(self):
        clear = open(self.data_file, 'w')
        clear.truncate()
        clear.close()