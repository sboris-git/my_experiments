import psycopg2

# https://stackoverflow.com/questions/37648667/python-how-to-initiate-and-close-a-mysql-connection-inside-a-class
class Database_Test(object):
    def __init__(self, db_local):
        self.db_local = db_local
        # self.db_conn = None
        # self.db_cursor = None

    def __del__(self):
        self.db_conn.close()

    def do_connect(self):
        self.db_conn = psycopg2.connect(**self.db_local)
        self.db_cursor = self.db_conn.cursor()

    def get_row(self, sql):
        self.db_cursor.execute(sql)
        self.resultset = self.db_cursor.fetchall()
        return self.resultset

db_config =  {
            'host':"127.0.0.1",                 # database host
            'port': 5432,                       # port
            'user':"postgres",                  # username
            'password':"SBoris",                # password
            'database':"testdb",                # database
            }


sql = "SELECT * FROM company WHERE salary > 2000"

obj = Database_Test(db_config)
obj.do_connect()
data = obj.get_row(sql)
for item in data:
    print(item)
