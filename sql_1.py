import sqlite3
# https://datascienceplus.com/sqlite-in-python/?fbclid=IwAR04v8Y3f8obMpU0Y0ezg7DT6g_ywDZQDHbCjVL4W8W3GaPaMWA90daSkao

connection = sqlite3.connect("company.db")
cursor = connection.cursor()

staff_data = [("William", "Shakespeare", "m", "1961-10-25"),
              ("Frank", "Schiller", "m", "1955-08-17"),
              ("Jane", "Wall", "f", "1989-03-14")]

for p in staff_data:
    format_str = """INSERT INTO employee (staff_number, fname, lname, gender, birth_date)
    VALUES (NULL, "{first}", "{last}", "{gender}", "{birthdate}");"""
    #print( 1, format_str )
    sql_command = format_str.format(first=p[0], last=p[1], gender=p[2], birthdate=p[3])
    cursor.execute(sql_command)
    #print( 2, sql_command )

cursor = connection.cursor()

cursor.execute("SELECT * FROM employee")
print("fetchall:")
result = cursor.fetchall()
for r in result:
    print(r)

cursor.execute("SELECT * FROM employee")
print("\nfetch one:")
res = cursor.fetchone()
print(res)

# never forget this, if you want the changes to be saved:
connection.commit()

connection.close()