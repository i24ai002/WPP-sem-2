word = input("enter a word: ")
result = []

for i, letter in enumerate(word):
    if i % 2 == 0:
        result.append(letter.lower())
    else:
        result.append(letter.upper())
    
print(result)