from datetime import date, timedelta


birthday = date(1974, 10, 4)
print(birthday)
print(birthday.weekday())

target_date = birthday + timedelta(days=1000)
print(target_date)
