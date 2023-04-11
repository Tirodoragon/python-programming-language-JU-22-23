length = 12
measure = '|'

for i in range(length):
    measure += "....|"
measure += '\n'

for i in range(length):
    measure += str(i)
    for j in range(5 - len(str(i+1))):
        measure += ' '

measure += str(length)
print(measure)