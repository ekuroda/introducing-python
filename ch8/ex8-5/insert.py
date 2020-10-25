import csv
import sqlite3

query = "insert into book values(?, ?, ?)"


def insert_book(curs, book):
    curs.execute(query, (book['title'], book['author'], book['year']))


with sqlite3.connect('books.db') as db:
    curs = db.cursor()
    with open('books.csv', 'rt') as f:
        books = csv.DictReader(f)
        for book in books:
            insert_book(curs, book)
    db.commit()
