import sqlite3

conn = sqlite3.connect('pelis.db')

conn.execute("CREATE TABLE Peliculas (id INTEGER PRIMARY KEY AUTOINCREMENT, LA id integer, nombre text, duracion integer )")
conn.close()