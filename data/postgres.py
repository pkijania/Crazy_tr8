from data.abstract import DataManager
import psycopg2

class PostgresDataBase(DataManager):
    def __init__(self):
        print("Transfering data to postgres data base")
        self.conn = psycopg2.connect(host = "localhost", dbname = "postgres", user = "postgres", password = "toster1111", port = 5432)
        self.cur = self.conn.cursor()

    def insert(self, price, date, ema_long, ema_short, macd, rsi, adx):
        insert_values = 'INSERT INTO crazy_tr8 (price, date, ema_long, ema_short, macd, rsi, adx) VALUES (%s, %s, %s, %s, %s, %s, %s)'
        values = [price, date, ema_long, ema_short, macd, rsi, adx]
        with self.conn.cursor() as cur:
            self.cur.execute(insert_values, values)
    
    def clean(self):
        clean_table = 'DELETE FROM crazy_tr8'
        with self.conn.cursor() as cur:
            self.cur.execute(clean_table)