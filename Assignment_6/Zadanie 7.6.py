import itertools
import random

print('(a)')

iter1 = itertools.cycle(range(0, 2))

for i in range(6):
    print(next(iter1))
    
print ('(b)')

iter2 = iter(lambda: random.choice(("N", "E", "S", "W")), 1)

for i in range(8):
    print(next(iter2))

print('(c)')

iter3 = itertools.cycle(range(0, 7))

for i in range(14):
    print(next(iter3))
    