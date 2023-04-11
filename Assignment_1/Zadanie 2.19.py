numbers = [394, 13, 9, 3, 26, 749, 2, 86, 656, 48]
numbers_3 = []

for number in numbers:
	numbers_3.append(str(number).zfill(3))

word = ' '.join(map(str, numbers_3))

print(word)