import sqlite3

con = sqlite3.connect('music_db.sqlite')
cur = con.cursor()
result = cur.execute("""SELECT Name
FROM Artist 
WHERE ArtistId IN 
(SELECT ArtistId FROM Album WHERE AlbumId IN 
(SELECT AlbumId FROM Track WHERE genreId IN
(SELECT genreId FROM genre WHERE name = ?)))
ORDER BY Name""", (a,)).fetchall()

print(*map(lambda x: x[0], result), sep='\n')
