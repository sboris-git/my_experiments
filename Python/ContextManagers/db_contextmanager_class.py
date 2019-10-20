# Python program shows the
# connection management

import psycopg2


class DbConnectionManager:

    def __init__(self, db_config_dict):
        self.db_config = db_config_dict
        # self.dbname = db_config_dict["database"]
        # self.hostname = db_config_dict["host"]
        # self.port = db_config_dict["port"]
        # self.username = db_config_dict["user"]
        # self.password = db_config_dict["password"]
        self._conn = None
        self._cursor = None

    def __enter__(self):
        self._conn = psycopg2.connect(**self.db_config)
                #                       database=self.dbname,
                #                       user = self.username,
                #                       password = self.password,
                #                       host = self.hostname,
                #                       port = self.port)
        self._cursor = self._conn.cursor()
        return self

    def __exit__(self, exc_type, exc_value, exc_traceback):
        self.commit()
        self.connection.close()

    @property
    def connection(self):
        return self._conn

    @property
    def cursor(self):
        return self._cursor

    def commit(self):
        self.connection.commit()

    def execute(self, sql):  # Optionally execute(self, sql, params=None)
        self.cursor.execute(sql)  # (sql, params or ())

    def fetchall(self):
        return self.cursor.fetchall()

    def fetchone(self):
        return self.cursor.fetchone()

    def query(self, sql):
        self.cursor.execute(sql)
        return self.fetchall()

# connecting to a localhost
db_config = {
            'host': "127.0.0.1",                 # database host
            'port': 5432,                        # port
            'user': "postgres",                  # username
            'password': "******",                # password
            'database': "testdb",                # database
            }

with DbConnectionManager(db_config) as db:
    # ID,NAME,AGE,ADDRESS,SALARY
    sql = '''
    SELECT 
        * 
    FROM 
        company 
    ORDER BY 
        name
    OFFSET 1
    FETCH FIRST 3 ROWS ONLY
    ;'''
    # db.execute(sql)
    # rows = db.fetchall()
    rows = db.query(sql)
    print('Selected database contains {} records'.format(len(rows)))
    for row in rows:
        print(row)
    print("Records read successfully")
