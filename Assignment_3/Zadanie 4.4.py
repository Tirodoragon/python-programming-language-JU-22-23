def fibonacci(n):
    a, b = 0, 1
    for i in range(n):
        a, b = b, a + b
    return a


inp = input("Wprowadz nieujemna liczbe calkowita: ")
try:
    inp = int(inp)
except ValueError:
    raise ValueError("To nie jest liczba calkowita!") from None

if inp < 0:
    raise ValueError("To nie jest nieujemna liczba calkowita!")

print(fibonacci(inp))
