x = 2; y = 3;
if (x > y):
    result = x;
else:
    result = y;
	
# powyzszy kod jest poprawny skladniowo

for i in "axby": if ord(i) < 100: print (i)

# powyzszy kod nie jest poprawny skladniowo, poniewaz jest to instrukcja zlozona i po kazdym dwukropku powinno byc przejscie do nowej linii oraz wciecie za kazdym razem, wyjatek stanowi ponizsza instrukcja prosta, kiedy jest tylko jeden dwukropek

for i in "axby": print (ord(i) if ord(i) < 100 else i)

# powyzszy kod jest poprawny skladniowo