import psycopg2

class PostgresDataBase:
    def __init__(self, data_file):
        self.data_file = data_file

    def transfer_data(self):
        conn = psycopg2.connect(host = "localhost", dbname = "postgres", user = "postgres", password = "toster1111", port = 5432)
        cur = conn.cursor()
        with open(self.data_file, 'r') as f:
            cur.copy_from(f, 'crazy_tr8', sep = ',')
        conn.commit()