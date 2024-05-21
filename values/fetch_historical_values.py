import csv

class HistoricalValueFetcher:
    def __init__(self, id_value):
        self.id_value = id_value
        self.list_of_values = []
        path = "D:\Giełda\Historyczne ceny bitcoina\XBTUSD_Q3.csv"
        with open(path, 'r') as file_csv:
            csv_reader = csv.reader(file_csv)
            self.list = list(csv_reader)
            self.selected_prices = [self.row[1] for self.row in self.list]
            self.selected_dates = [self.row[0] for self.row in self.list]
            for self.i in range(1,101):
                self.list_of_values.extend([(self.i, self.selected_prices[self.i], self.selected_dates[self.i])])

    def get_historical_price(self):
        try:
            price = self.list_of_values[self.id_value][1]
            return price
        except Exception as e:
            raise Exception(f'An error has occured due to: {e}')

    def get_historical_date(self):
        try:
            date = self.list_of_values[self.id_value][2]
            return date
        except Exception as e:
            raise Exception(f'An error has occured due to: {e}')
