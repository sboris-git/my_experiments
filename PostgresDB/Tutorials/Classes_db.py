import psycopg2


class PostgresDB:

    def __init__(self, config):
        self.config = config

    def connect_db(self):
        self.conn = psycopg2.connect(**self.config)

    def exe_sql(self, query):
        '''Execute SQL query'''
        self.cursor = self.conn.cursor()
        print(query)
        #return self.cursor.execute(query)

    def close_conn(self):
        '''Commit changes in db and close connection'''
        self.conn.commit()
        self.conn.close()

    # def __del__( self ):
    #     self.connection.close()
    #     self.cursor.close()

    def print_db(self):
        # self.cursor = self.conn.cursor()
        # sql = '''SELECT * FROM COMPANY;'''
        # self.cursor.execute(sql)
        rows = self.cursor.fetchall()
        print( 'Database contains {} records'.format( len( rows ) ) )
        for row in rows:
            print( row )





# Create an instance of a Class object

db_config =  {
            'host':"127.0.0.1",                 # database host
            'port': 5432,                       # port
            'user':"postgres",                  # username
            'password':"SBoris",                # password
            'database':"testdb",                # database
            }

db_instance = PostgresDB(db_config)
print("Init instance successfully")
db_instance.connect_db()
print("Opened database successfully")
query = '''SELECT * FROM company'''
data = db_instance.exe_sql(query)
print(len(data))
for row in data:
    print(row)
print("Query executed successfully")
db_instance.close_conn()
print("Connection closed")
