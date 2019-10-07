import psycopg2

conn = psycopg2.connect(database="dvdrental",
                        user = "postgres",
                        password = "SBoris",
                        host = "127.0.0.1",
                        port = "5432")
# http://www.postgresqltutorial.com/postgresql-python/connect/

print("Opened database successfully")

cur = conn.cursor()
sql = '''
SELECT * FROM staff;
'''
cur.execute(sql)
rows = cur.fetchall()
print('Database contains {} records'.format(len(rows)))
for row in rows:
    print(row)
# cur = conn.cursor()
conn.close()
