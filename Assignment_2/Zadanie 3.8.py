x = [(1, 2), (2, 3, 4), (4, 5, 6, 7), (7, 0)]
y = [(9, 8), (7, 0), (7, 6, 5), (5, 4, 3, 2)]

setX = set()
setY = set()

for e in y:
    setY.update(set(e))

for e in x:
    setX.update(set(e))

print(setY.intersection(setX))
print(setY.union(setX))