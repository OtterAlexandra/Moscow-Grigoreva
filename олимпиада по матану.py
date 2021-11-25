import sqlite3

con = sqlite3.connect('films_db.sqlite')

cur = con.cursor()

a = 2010
b = cur.execute("""SELECT id FROM Films WHERE year = ?""", (a,)).fetchone()
print(*b)
c = cur.execute("""SELECT title FROM Films WHERE id = ?""", (*b,)).fetchall()

print(*c)