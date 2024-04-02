# Module deletes old data and adds new data to a postgres data base

from data.abstract import DataManager
import psycopg2
from urllib.parse import urlparse

class PostgresDataBase(DataManager):
    """Class providing "insert" and "clean" methods that 
    deletes or adds data to a postgres data base"""
    def __init__(self, conStr):
        """Get a connection attribute and connect to a data base"""
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
        """Insert data into a postgres data base"""
        insert_values = '''INSERT INTO history (price, date, ema_long, ema_short, macd, rsi, adx) 
        VALUES (%s, %s, %s, %s, %s, %s, %s)'''
        values = [price, date, ema_long, ema_short, macd, rsi, adx]
        with self.conn.cursor() as cur:
            cur.execute(insert_values, values)

    def clean(self):
        """Erase data into a postgres data base"""
        clean_table = 'DELETE FROM history'
        with self.conn.cursor() as cur:
            cur.execute(clean_table)
