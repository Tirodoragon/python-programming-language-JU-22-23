x = 2
y = 4
field = '\n'

for i in range(x):
    for j in range(y):
        field += "+---"
    field += "+\n"
    
    for j in range(y):
        field += "|   "
    field += "|\n"

for i in range(y):
    field += "+---"
field += "+\n"
print(field)