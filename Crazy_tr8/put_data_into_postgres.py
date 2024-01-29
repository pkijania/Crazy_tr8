import psycopg2

class PostgresDataBase:
    def __init__(self):
        print("Transfering data to postgres data base")

    def transfer_data(self, price, date, ema_long, ema_short, macd, rsi, adx):
        conn = psycopg2.connect(host = "localhost", dbname = "postgres", user = "postgres", password = "toster1111", port = 5432)
        cur = conn.cursor()
        insert_values = 'INSERT INTO crazy_tr8 (price, date, ema_long, ema_short, macd, rsi, adx) VALUES (%s, %s, %s, %s, %s, %s, %s)'
        values = [price, date, ema_long, ema_short, macd, rsi, adx]
        cur.execute(insert_values, values)
        conn.commit()