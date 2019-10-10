import config
import psycopg2

# The structure of config.py file
# db_config = {
#             'host': "localhost",                 # database host
#             'port': port,                        # port
#             'user': "localuser",                 # username
#             'password': "sequre_pass",           # password
#             'database': "library",               # database
# }

class DB(object):
    def __init__(self, config):
        self.config = config
        self.conn = psycopg2.connect(**self.config)

    def __del__(self):
        self.conn.close()

    def get_data(self, sql):
        with self.conn.cursor() as cursor:
            cursor.execute(sql)
            self.conn.commit()
            return cursor.fetchall()

    def count_frequency(self, sql):
        with self.conn.cursor() as cursor:
            cursor.execute(sql)
            self.conn.commit()
            return cursor.fetchall()




obj1 = DB(config)

query = ''' 
SELECT HUMANS.id, HUMANS.begin_name, HUMANS.end_name, \
       BOOKS.id, BOOKS.author, BOOKS.name, \
       READ_RETURN.id_user, READ_RETURN.id_book, READ_RETURN.is_returned
FROM ((HUMAN
INNER JOIN READ_RETURN ON HUMANS.id = READ_RETURN.id_user)
INNER JOIN BOOKS ON BOOKS.id = READ_RETURN.id_book);
'''
rows = obj1.get_data(query)
for item in rows:
    print(item)
query2 = '''     
obj.count_frequency(query2)
'''


Write code for next requirements:
  2. Write class for getting data from tables
  3. Write class for counting how often any human has read each book