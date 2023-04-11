line = "words length sum"

words = line.split()
    
number = sum([len(x) for x in words])

print(number)