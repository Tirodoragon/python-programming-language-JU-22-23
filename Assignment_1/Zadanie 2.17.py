line = """this is
a multiline
Python string"""

words = line.split()

print(sorted(words))

print(sorted(words, key=len))