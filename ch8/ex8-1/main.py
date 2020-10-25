test1 = "This is a test of the emergency text system"

with open("test.txt", "wt") as f:
    f.write(test1)

with open("test.txt", "rt") as f:
    t = f.read()

print(t == test1)
