# Python program shows the
# connection management

import psycopg2


class DBConnectionManager:

    def __init__(self,dbname, hostname, username, password):
        self.dbname = dbname,
        self.hostname = hostname
        self.port = 5432
        self.username = username
        self.password = password
        self.connection = None

    def __enter__(self):
        self.connection = psycopg2.connect(self.dbname, self.hostname, self.port, self.username, self.password)
        return self

    def __exit__(self, exc_type, exc_value, exc_traceback):
        self.connection.close()

# connecting to a localhost
conf = ("dbname='dvdrental'",
        "host='localhost'",
        "user='postgres'",
        "password='SBoris'")

print(*conf)
with DBConnectionManager(*conf) as postgreSQL:
    curs = postgreSQL.cursor()
    sql = '''
    SELECT 
        * 
    FROM 
        company 
    OFFSET 5
    FETCH FIRST 7 ROWS ONLY
    ;'''
    curs.execute(sql)
    rows = curs.fetchall()
    print('Database contains {} records'.format(len(rows)))
    for row in rows:
        print(row)
    print("Records read successfully")