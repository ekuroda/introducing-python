from datetime import datetime

today = datetime.now().astimezone()

with open('today.txt', 'tw') as f:
    f.write(today.isoformat())

with open('today.txt', 'tr') as f:
    today_string = f.read()

today_parsed = datetime.fromisoformat(today_string)

print(today_parsed)
