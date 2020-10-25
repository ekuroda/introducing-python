import sqlite3

with sqlite3.connect('books.db') as db:
    curs = db.execute('select title from book order by title')
    for row in curs:
        print(row)

    curs = db.execute('select * from book order by year')
    for row in curs:
        print(row)
