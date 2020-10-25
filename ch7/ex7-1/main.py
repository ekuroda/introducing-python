import unicodedata
mystery = "\U0001f4a9"
print(mystery)
print(unicodedata.name(mystery))

pop_bytes = mystery.encode('utf-8')
print(pop_bytes)

pop_string = pop_bytes.decode('utf-8')
print(pop_string)

print(pop_string == mystery)
