i = None
o = ""

while True:
    i = input('Wpisz liczbe rzeczywista albo "stop": ')

    if i == "stop":
        break

    try:
        i = float(i)
    except ValueError:
        print("Blad, wpisano napis zamiast liczby!")
        continue

    o = " ".join((str(i), str(i * i * i)))              #  mnozenie ma mniejsza zlozonosc niz pow i **
    print(o)