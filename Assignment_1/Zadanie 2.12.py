line = "place your train high on net"

words = line.split()

word = ""

for w in words:
	word += w[0]
    
print(word)

word = ""

for w in words:
	word += w[-1]
    
print(word)