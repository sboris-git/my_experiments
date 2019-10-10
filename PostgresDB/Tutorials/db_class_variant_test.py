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

    def print_query(self, sql):
        with self.conn.cursor() as cursor:
            cursor.execute(sql)
            self.conn.commit()
            rows = cursor.fetchall()
        for item in rows:
            print( item )


<<<<<<< HEAD


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


# Write code for next requirements:
#   2. Write class for getting data from tables
#   3. Write class for counting how often any human has read each book
# =======
db_config = {
            'host': "127.0.0.1",                 # database host
            'port': 5432,                        # port
            'user': "postgres",                  # username
            'password': "SBoris",                # password
            'database': "dvdrental",             # database
}
query_sql = '''SELECT * FROM film LIMIT 5'''

obj1 = DB(db_config)
rows = obj1.print_query(query_sql)
# BOOKS(id, author, name, genre)
# READ_RETURN(book_id, user_id, onhand, quantity)
# HUMAN(id, first_name, midle_name, last_name)

''' +actor – (actor_id, first_name, last_name, last_update) 
            stores actors data including first name and last name.
    +category -- (category_id, name, last_update) 
            – stores film’s categories data.
    +country – (country_id, country, last_update) stores the country names.
    +language -- (language_id, name, last_update)
    '''
# for item in rows:
#     print(item)

>>>>>>> 628e89e1b1e83ed8a4f942d920740c6b1f112480
