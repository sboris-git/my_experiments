import sqlite3

connection = sqlite3.connect("chinook.db")
cursor = connection.cursor()

# delete
#cursor.execute("""DROP TABLE employee;""")

#Create SQL tables in Python

# https://www.sqlitetutorial.net/sqlite-join/
# https://www.sqlitetutorial.net/sqlite-inner-join/
# https://www.sqlitetutorial.net/sqlite-cross-join/
# https://www.sqlitetutorial.net/sqlite-full-outer-join/
# https://www.sqlitetutorial.net/sqlite-self-join/
# https://www.sqlitetutorial.net/sqlite-union/
# https://www.sqlitetutorial.net/sqlite-count-function/

sql_command = """
SELECT
    trackid,
    name,
    tracks.albumid AS album_id_tracks,
    albums.albumid AS album_id_albums,
    title
FROM
    tracks
    INNER JOIN albums ON albums.albumid = tracks.albumid;
"""
cursor.execute(sql_command)
print("fetchall:")
res = cursor.fetchall()
for r in res:
    print(r)

# never forget this, if you want the changes to be saved:
#connection.commit()

connection.close()

cursor.execute('''
SELECT
   albumid, COUNT(*)
FROM
   tracks
GROUP BY
   albumid
HAVING COUNT(*) > 25
''')
print("fetchall:")
albums = cursor.fetchall()
for album in albums:
    print(album)

# never forget this, if you want the changes to be saved:
connection.commit()
connection.close()
