def factorial(n):
    f = 1
    
    while n >= 1:
        f = f * n
        n -= 1

    return f
    
    
inp = input("Wprowadz nieujemna liczbe calkowita: ")
try:
    inp = int(inp)
except ValueError:
    raise ValueError("To nie jest liczba calkowita!") from None

if inp < 0:
    raise ValueError("To nie jest nieujemna liczba calkowita!")
    
print(factorial(inp))
