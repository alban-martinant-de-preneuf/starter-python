userWord = input("Entrez un mot : ")
listUserWord = list(userWord)
nextWord = ""

index = -1
for letter in userWord:
    if listUserWord[index] != listUserWord[index - 1]:
        listUserWord[index], listUserWord[index - 1] = listUserWord[index - 1], listUserWord[index]
        break
    else:
        index -= 1

for char in listUserWord:
    nextWord += char

print(nextWord)
