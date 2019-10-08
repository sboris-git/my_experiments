import psycopg2


class DB(object):
    def __init__(self, config):
        self.config = config
        self.conn = psycopg2.connect(**self.config)

    def __del__(self):
        self.conn.close()

    def query(self, sql):
        with self.conn.cursor() as cursor:
            cursor.execute(sql)
            self.conn.commit()
            return cursor.fetchall()


db_config = {
            'host': "127.0.0.1",                 # database host
            'port': 5432,                        # port
            'user': "postgres",                  # username
            'password': "SBoris",                # password
            'database': "dvdrental",                # database
}

obj1 = DB(db_config)
rows = obj1.query('''SELECT * FROM actor LIMIT 5 OFFSET 2''')
for item in rows:
    print(item)
