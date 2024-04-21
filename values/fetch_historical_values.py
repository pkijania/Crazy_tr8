import csv

class HistoricalValueFetcher:
    def __init__(self):
        list_of_values = []
        path = "Github/Crazy_tr8/historical_data/XBTUSD_Q3.csv"
        with open(path, 'r') as file_csv:
            csv_reader = csv.reader(file_csv)
            for self.row in csv_reader:
                list_of_values.append(self.row)

    def get_historical_price(self):
        try:
            return self.row[1]
        except Exception as e:
            raise Exception(f'An error has occured due to: {e}')

    def get_historical_date(self):
        try:
            return self.row[0]
        except Exception as e:
            raise Exception(f'An error has occured due to: {e}')
