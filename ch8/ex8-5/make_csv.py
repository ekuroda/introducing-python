text = '''title,author,year
The Weirdstone of Brisingamen,Alan Garner,1960
Padido Street Station,China Miéville,2000
Thud!,Terry Pretchett,2005
The Spellman Files,Lisa Lutz,2007
Small Gods,Terry Pratchett,1992
'''

with open('books.csv', 'wt') as f:
    f.write(text)
