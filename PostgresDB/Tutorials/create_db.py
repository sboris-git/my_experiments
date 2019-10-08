import psycopg2

con = psycopg2.connect(dbname='postgres',
                       user='boris',
                       host='localhost',
                       password='SBoris')
# create db
# con.autocommit = True
# cur = con.cursor()
# cur.execute('CREATE DATABASE {};'.format('postgres_py_db'))


con.close()
