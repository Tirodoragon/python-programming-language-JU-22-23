L = [3, 5, 4] ; L = L.sort() # L.sort() nic nie zwraca tylko modyfikuje obecna liste, powinno byc bez przypisania do zmiennej, w tym przypadku L jest ustawione na None
x, y = 1, 2, 3 #             # trzy wartosci przypisywane do dwoch zmiennych
X = 1, 2, 3 ; X[1] = 4       # nie mozliwe przypisanie, poniewaz X to nie lista a krotka i nie podlega zmianom
X = [1, 2, 3] ; X[3] = 4     # nie ma indeksu 3 w liscie X
X = "abc" ; X.append("d")    # string nie ma metody append()
L = list(map(pow, range(8))) # pow() potrzebuje dwoch argumentow