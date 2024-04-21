"""Module deletes old data and adds new data to a postgres data base"""

from urllib.parse import urlparse
import psycopg2
from data.abstract import DataManager

class PostgresHitsoricalDataBase(DataManager):
    """Class providing "insert" and "clean" methods that 
    deletes or adds data to a postgres data base"""
    def __init__(self, con_str):
        """Get a connection attribute and connect to a data base"""
        print("Transfering data to postgres data base")
        p = urlparse(con_str)
        pg_connection_dict = {
            'dbname': p.path[1:],
            'user': p.username,
            'password': p.password,
            'port': p.port,
            'host': p.hostname
        }
        self.conn = psycopg2.connect(**pg_connection_dict)
        self.conn.set_session(autocommit=True)

    def insert(self, id_value, price, date, ema_long, ema_short, macd, rsi, adx):
        """Insert data into a postgres data base"""
        insert_values = '''INSERT INTO test (id, price, date, ema_long, ema_short, macd, rsi, adx)
        VALUES (%s, %s, %s, %s, %s, %s, %s, %s)'''
        values = [id_value, price, date, ema_long, ema_short, macd, rsi, adx]
        with self.conn.cursor() as cur:
            cur.execute(insert_values, values)

    def clean(self):
        """Erase data into a postgres data base"""
        clean_table = 'DELETE FROM test'
        with self.conn.cursor() as cur:
            cur.execute(clean_table)
