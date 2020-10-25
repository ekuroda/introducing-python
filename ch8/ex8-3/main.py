import csv

with open("books.csv", "rt") as f:
    c = csv.DictReader(f)
    books = [{k: r[k] for k in r} for r in c]

print(books)
