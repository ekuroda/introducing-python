import sqlite3

db = sqlite3.connect('books.db')
curs = db.cursor()
curs.execute('create table book(title text, author text, year int)')
db.commit()
