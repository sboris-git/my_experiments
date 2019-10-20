# Python program shows the
# connection management

import psycopg2


class DBConnectionManager:

    def __init__(self, db_config_dict):
        self.dbname = db_config_dict["database"]
        self.hostname = db_config_dict["host"]
        self.port = db_config_dict["port"]
        self.username = db_config_dict["user"]
        self.password = db_config_dict["password"]

    def __enter__(self):
        self.connection = psycopg2.connect(database=self.dbname,
                                           user = self.username,
                                           password = self.password,
                                           host = self.hostname,
                                           port = self.port)
        return self.connection

    def __exit__(self, exc_type, exc_value, exc_traceback):
        self.connection.close()


# connecting to a localhost
db_config =  {
            'host':"127.0.0.1",                 # database host
            'port': 5432,                       # port
            'user':"postgres",                  # username
            'password':"*****",                # password
            'database':"testdb",                # database
            }

# print(db_config)
with DBConnectionManager(db_config) as postgreSQL:
    curs = postgreSQL.cursor()
    # ID,NAME,AGE,ADDRESS,SALARY
    sql = '''
            SELECT 
                * 
            FROM 
                company 
            ORDER BY 
                 name
            OFFSET 2
            FETCH FIRST 2 ROWS ONLY
            ;'''
    curs.execute(sql)
    rows = curs.fetchall()
    print('Selected database contains {} records'.format(len(rows)))
    for row in rows:
        print(row)
    print("Records read successfully")