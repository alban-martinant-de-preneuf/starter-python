letters = input("Entrez vos lettres : ")
possibleWords = []

letterPoints = {
    "e" : 1,
    "a" : 1,
    "i" : 1,
    "n" : 1,
    "o" : 1,
    "r" : 1,
    "s" : 1,
    "t" : 1,
    "u" : 1,
    "l" : 1,
    "d" : 2,
    "g" : 2,
    "m" : 2,
    "b" : 3,
    "c" : 3,
    "p" : 3,
    "f" : 4,
    "h" : 4,
    "v" : 4,
    "j" : 8,
    "q" : 8,
    "k" : 10,
    "w" : 10,
    "x" : 10,
    "y" : 10,
    "z" : 10
}

with open("dico2.txt") as dico:
    possibleWords = dico.readlines()

# #Enlever les caracères \n
# for i in range(0, len(possibleWords)):
#     possibleWords[i] = possibleWords[i][:-1]

#Enlever les \n, les majuscules, les accents, remplacer caractères spéciaux
forbChar = ("ÀÁÂÆÇÈÉÊËÌÍÎÏÑÒÓÔŒÙÚÛÜÝŸàáâæçèéêëìíîïñòóôœùúûüýÿ\nABCDEFGHIJKLMNOPQRSTUVWXYZ") 
correspondForChar = {
    "À" : "a",
    "Á" : "a",
    "Â" : "a",
    "Æ" : "ae",
    "Ç" : "c",
    "È" : "e",
    "É" : "e",
    "Ê" : "e",
    "Ë" : "e",
    "Ì" : "i",
    "Í" : "i",
    "Î" : "i",
    "Ï" : "i",
    "Ñ" : "n",
    "Ò" : "o",
    "Ó" : "o",
    "Ô" : "o",
    "Œ" : "oe",
    "Ù" : "u",
    "Ú" : "u",
    "Û" : "u",
    "Ü" : "u",
    "Ý" : "y",
    "Ÿ" : "y",
    "à" : "a",
    "á" : "a",
    "â" : "a",
    "æ" : "ae",
    "ç" : "c",
    "è" : "e",
    "é" : "e",
    "ê" : "e",
    "ë" : "e",
    "ì" : "i",
    "í" : "i",
    "î" : "i",
    "ï" : "i",
    "ñ" : "n",
    "ò" : "o",
    "ó" : "o",
    "ô" : "o",
    "œ" : "oe",
    "ù" : "u",
    "ú" : "u",
    "û" : "u",
    "ü" : "u",
    "ý" : "y",
    "ÿ" : "y",
    "\n" : "",
    "A" : "a",
    "B" : "b",
    "C" : "c",
    "D" : "d",
    "E" : "e",
    "F" : "f",
    "G" : "g",
    "H" : "h",
    "I" : "i",
    "J" : "j",
    "K" : "k",
    "L" : "l",
    "M" : "m",
    "N" : "n",
    "O" : "o",
    "P" : "p",
    "Q" : "q",
    "R" : "r",
    "S" : "s",
    "T" : "t",
    "U" : "u",
    "V" : "v",
    "W" : "w",
    "X" : "x",
    "Y" : "y",
    "Z" : "z"
    }

for i in range(0, len(possibleWords)):
    tmpWord = []
    for letter in possibleWords[i]:
        tmpWord.append(letter)
    for j in range(0, len(tmpWord)):
        if tmpWord[j] in forbChar:
            tmpWord[j] = correspondForChar[tmpWord[j]]
    possibleWords[i] = "".join(tmpWord)


#enlever les mots qui contiennent des lettres que nous n'avons pas :
toRemove = []

for i in range(0, len(possibleWords)):
    for letterInWord in possibleWords[i]:
        if letterInWord not in letters:
            if  possibleWords[i] not in toRemove:
                toRemove.append(possibleWords[i])
                break

for word in toRemove:
    possibleWords.remove(word)

#garder que les mots possible à écrire entièrement avec nos lettres
toRemove = []

for i in range(0, len(possibleWords)):
    remainingLetters = list(letters)
    for wordLetter in possibleWords[i]:
        if wordLetter in remainingLetters:
            remainingLetters.remove(wordLetter)
        else:
            toRemove.append(possibleWords[i])
            break

for word in toRemove:
    possibleWords.remove(word)

#compter les points
wordPoints = []
i = 0
for word in possibleWords:
    wordPoints.append([word, 0])
    for letter in word:
        wordPoints[i][1] += letterPoints[letter]
    i += 1

#trier les résultats
swapped = True
while swapped:
    swapped = False
    for i in range(0, len(wordPoints) - 1):
        if wordPoints[i + 1][1] > wordPoints[i][1]:
            wordPoints[i + 1], wordPoints[i] = wordPoints[i], wordPoints[i + 1]
            swapped = True

#Afficher les résultats
for i in range(0, len(wordPoints)):
    print("{0} : {1} point(s)".format(wordPoints[i][0], wordPoints[i][1]))
