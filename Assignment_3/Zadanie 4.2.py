def make_ruler(n):
    ruler = '|'

    for i in range(n):
        ruler += "....|"
    ruler += '\n'

    for i in range(n):
        ruler += str(i)
        for j in range(5 - len(str(i + 1))):
            ruler += ' '

    ruler += str(n)

    return ruler


def make_grid(rows, cols):
    grid = '\n'

    for i in range(rows):
        for j in range(cols):
            grid += "+---"
        grid += "+\n"

        for j in range(cols):
            grid += "|   "
        grid += "|\n"

    for i in range(cols):
        grid += "+---"
    grid += "+\n"

    return grid


inp1 = input("Wprowadz liczbe calkowita miarki wieksza lub rowna 1: ")
try:
    inp1 = int(inp1)
except ValueError:
    raise ValueError("To nie jest liczba calkowita!") from None

if inp1 < 1:
    raise ValueError("To nie jest liczba calkowita wieksza lub rowna 1!")

inp2 = input("Wprowadz liczbe calkowita wierszy wieksza lub rowna 1: ")
try:
    inp2 = int(inp2)
except ValueError:
    raise ValueError("To nie jest liczba calkowita!") from None

if inp2 < 1:
    raise ValueError("To nie jest liczba calkowita wieksza lub rowna 1!")

inp3 = input("Wprowadz liczbe calkowita kolumn wieksza lub rowna 1: ")
try:
    inp3 = int(inp3)
except ValueError:
    raise ValueError("To nie jest liczba calkowita!") from None

if inp3 < 1:
    raise ValueError("To nie jest liczba calkowita wieksza lub rowna 1!")

print(make_ruler(inp1))
print(make_grid(inp2, inp3))
