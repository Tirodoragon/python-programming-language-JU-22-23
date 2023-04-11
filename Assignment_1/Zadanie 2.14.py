line = "the longest word"

words = line.split()

the_longest_word = ''

for word in words:
    if len(word) > len(the_longest_word):
        the_longest_word = word
    
print(the_longest_word, len(the_longest_word))

the_longest_word = ''

length = 0

for word in words:
    if len(word) > len(the_longest_word):
        the_longest_word = word
        length = len(word)

print(length)