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
query_sql = '''SELECT * FROM actor LIMIT 5'''

obj1 = DB(db_config)
rows = obj1.print_query(query_sql)

''' actor – stores actors data including first name and last name.
    film – stores films data such as title, release year, length, rating, etc.
    film_actor – stores the relationships between films and actors.
    category – stores film’s categories data.
    film_category- stores the relationships between films and categories.
    store – contains the store data including manager staff and address.
    inventory – stores inventory data.
    rental – stores rental data.
    payment – stores customer’s payments.
    staff – stores staff data.
    customer – stores customers data.
    address – stores address data for staff and customers
    city – stores the city names.
    country – stores the country names.'''
# for item in rows:
#     print(item)

