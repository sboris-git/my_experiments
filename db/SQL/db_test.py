import sqlite3

con = sqlite3.connect(r'/home/dad/Documents/db/chinook.db')
cursorObj = con.cursor()
'''
command = "SELECT albumid, COUNT(trackid)\
        FROM tracks\
        GROUP BY albumid;"

doesnt work
command = "SELECT albumid, COUNT(trackid) \
FROM tracks \
WHERE COUNT(albumid) BETWEEN 18 AND 20;"
# GROUP BY albumid \
# HAVING albumid = 1;"
'''
command = '''\
SELECT
    tracks.AlbumId,
    title,
    SUM(Milliseconds) AS length
FROM
    tracks
INNER JOIN albums ON albums.AlbumId = tracks.AlbumId
GROUP BY
    tracks.AlbumId 
HAVING
    length > 60000000;'''

# SELECT
#    albumid,
#    COUNT(trackid)
# FROM
#    tracks
# GROUP BY
#    albumid
# HAVING
#    COUNT(albumid) BETWEEN 18 AND 20
# ORDER BY albumid;'''

cursorObj.execute(command)
rows = cursorObj.fetchall()

for row in rows:
    print(row)

con.commit()