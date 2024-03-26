from data.abstract import DataManager
import psycopg2
from urllib.parse import urlparse

class PostgresDataBase(DataManager):
    def __init__(self):
        print("Transfering data to postgres data base")
        conStr = "schema://user:password@host:port/dbname"
        p = urlparse(conStr)
        pg_connection_dict = {
            'dbname': p.hostname,
            'user': p.username,
            'password': p.password,
            'port': p.port,
            'schema': p.scheme
        }
        print(pg_connection_dict)
        self.conn = psycopg2.connect(**pg_connection_dict)
        print(self.conn)
        self.conn.set_session(autocommit=True)

    def insert(self, price, date, ema_long, ema_short, macd, rsi, adx):
        insert_values = 'INSERT INTO crazy_tr8 (price, date, ema_long, ema_short, macd, rsi, adx) VALUES (%s, %s, %s, %s, %s, %s, %s)'
        values = [price, date, ema_long, ema_short, macd, rsi, adx]
        with self.conn.cursor() as cur:
            cur.execute(insert_values, values)
    
    def clean(self):
        clean_table = 'DELETE FROM crazy_tr8'
        with self.conn.cursor() as cur:
            cur.execute(clean_table)