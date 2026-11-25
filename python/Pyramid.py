rows = 10
for i in range(1, rows + 1):
    spaces = " " * (rows - i)
    print(spaces + "* " * i)

for i in range(rows - 1, 0, -1):
    spaces = " " * (rows - i)
    print(spaces + "* " * i)