import sqlite3
# https://datascienceplus.com/sqlite-in-python/?fbclid=IwAR04v8Y3f8obMpU0Y0ezg7DT6g_ywDZQDHbCjVL4W8W3GaPaMWA90daSkao
# https://www.youtube.com/watch?v=2HVMiPPuPIM
connection = sqlite3.connect("chinook.db")
cursor = connection.cursor()
# format_str = """DELETE FROM Customer"""
# sql_command = format_str
# cursor.execute(sql_command)

# sql_command = "DROP TABLE Customer"
# cursor.execute(sql_command)


# format_str = """DELETE FROM Customer WHERE Id<6"""
# sql_command = format_str
# cursor.execute(sql_command)

# sql_command = """CREATE TABLE City (
#     CityId INTEGER PRIMARY KEY,
#     CityName TEXT NOT NULL
# );"""
# cursor.execute(sql_command)
#
#
# City_data = [(1, "Kanzas City"),
#               (2, "New York"),
#               (3, "Houston")]
#
# for p in City_data:
#     format_str = """INSERT INTO City (CityId, CityName)
#     VALUES ("{CityId}", "{CityName}");"""
#     sql_command = format_str.format(CityId=p[0], CityName=p[1])
#     cursor.execute(sql_command)

# sql_command = """CREATE TABLE Customer (
#     CustomerId INTEGER PRIMARY KEY,
#     CityId TEXT NOT NULL,
#     CustomerName TEXT NOT NULL
# );"""
# cursor.execute(sql_command)
# staff_data = [(1, 1, "Bob Smith"),
#               (2, 1, "Sally Smith"),
#               (3, 2, "Tom Smith"),
#               (4, "NULL", "Mary Smith")]
#
# for p in staff_data:
#     format_str = """INSERT INTO Customer (CustomerId, CityId, CustomerName)
#     VALUES ("{CustomerId}", "{CityId}", "{CustomerName}");"""
#     sql_command = format_str.format(CustomerId=p[0], CityId=p[1], CustomerName=p[2])
#     cursor.execute(sql_command)

# cursor = connection.cursor()
# cursor.execute("SELECT * FROM Customer")
# print("fetchall:")
# result = cursor.fetchall()
# for r in result:
#     print(r)
#
# cursor.execute("SELECT * FROM Customer")
# print("\nfetch one:")
# res = cursor.fetchone()
# print(res)

# sql_command = '''
# SELECT * FROM Customer Inner Join City
# on Customer.CityId=City.CityId'''
# cursor.execute(sql_command)

# sql_command = '''
# SELECT * FROM Customer Left Join City
# on Customer.CityId=City.CityId'''
# cursor.execute(sql_command)
#

# Not full Emulation of Right Join
# sql_command = '''
# SELECT * FROM City Left Join Customer
# on Customer.CityId=City.CityId'''
# cursor.execute(sql_command)

# Not supported
# sql_command = '''
# SELECT * FROM City Full Join Customer
# on Customer.CityId=City.CityId'''
# cursor.execute(sql_command)

print("fetchall:")
result = cursor.fetchall()
for r in result:
    print(r)

# # never forget this, if you want the changes to be saved:
connection.commit()

connection.close()
