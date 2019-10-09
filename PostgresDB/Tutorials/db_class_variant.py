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

    def print_query(self, sql):
        with self.conn.cursor() as cursor:
            cursor.execute(sql)
            self.conn.commit()
            rows = cursor.fetchall()
        for item in rows:
            print( item )


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

