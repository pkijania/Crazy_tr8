from data.abstract import DataManager
import psycopg2
from urllib.parse import urlparse

class PostgresDataBase(DataManager):
    def __init__(self, conStr):
        print("Transfering data to postgres data base")
        p = urlparse(conStr)
        pg_connection_dict = {
            'dbname': p.path[1:],
            'user': p.username,
            'password': p.password,
            'port': p.port,
            'host': p.hostname
        }
        self.conn = psycopg2.connect(**pg_connection_dict)
        self.conn.set_session(autocommit=True)

    def insert(self, price, date, ema_long, ema_short, macd, rsi, adx):
        insert_values = 'INSERT INTO history (price, date, ema_long, ema_short, macd, rsi, adx) VALUES (%s, %s, %s, %s, %s, %s, %s)'
        values = [price, date, ema_long, ema_short, macd, rsi, adx]
        with self.conn.cursor() as cur:
            cur.execute(insert_values, values)
    
    def clean(self):
        clean_table = 'DELETE FROM history'
        with self.conn.cursor() as cur:
            cur.execute(clean_table)