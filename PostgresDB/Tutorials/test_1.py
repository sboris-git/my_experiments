import psycopg2

conn = psycopg2.connect(database="testdb", user = "postgres", password = "SBoris", host = "127.0.0.1", port = "5432")

print("Opened database successfully")

# cur = conn.cursor()
# cur.execute('''CREATE TABLE COMPANY
#       (ID INT PRIMARY KEY     NOT NULL,
#       NAME           TEXT    NOT NULL,
#       AGE            INT     NOT NULL,
#       ADDRESS        CHAR(50),
#       SALARY         REAL);''')
# print("Table created successfully")

# cur = conn.cursor()
# cur.execute("INSERT INTO COMPANY (ID,NAME,AGE,ADDRESS,SALARY) \
#       VALUES (1, 'Paul', 32, 'California', 20000.00 )")
# cur.execute("INSERT INTO COMPANY (ID,NAME,AGE,ADDRESS,SALARY) \
#       VALUES (2, 'Allen', 25, 'Texas', 15000.00 )")
# cur.execute("INSERT INTO COMPANY (ID,NAME,AGE,ADDRESS,SALARY) \
#       VALUES (3, 'Teddy', 23, 'Norway', 20000.00 )")
# cur.execute("INSERT INTO COMPANY (ID,NAME,AGE,ADDRESS,SALARY) \
#       VALUES (4, 'Mark', 25, 'Rich-Mond ', 65000.00 )")
# conn.commit()

cur = conn.cursor()
sql = '''
SELECT * FROM COMPANY;
'''
cur.execute(sql)
rows = cur.fetchall()
print('Database contains {} records'.format(len(rows)))
for row in rows:
    print(row)
# print("Records created successfully")
# conn.commit()
conn.close()