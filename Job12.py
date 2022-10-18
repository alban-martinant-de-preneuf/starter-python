# import re

# nbWords = 0

# with open("data.txt") as data:
#    findedWords = re.findall(r"\b[a-zA-Z]{1,}\b", data.read())

# for mot in findedWords:
#     nbWords += 1

# print("Il y a " + str(nbWords) + " mots dans le texte.")

##Sans regex :
import os

charsAllowed = "abcdefghijklmnopqrstuvwxyz \nABCDEFGHIJKLMNOPQRSTUVWXYZ"
nbOfWords = 0

dataFile = open("data.txt")
tmpData = open("tmpData.txt", "a")

for char in dataFile.read():
    if char in charsAllowed:
        tmpData.write(char)

dataFile.close()
tmpData.close()

tmpData = open("tmpData.txt", "r")

for char in tmpData.read():
    if (char == " " or char == "\n") and (previousChar != " " and previousChar != "\n"):
        nbOfWords += 1
    previousChar = char

tmpData.close()
os.remove("tmpData.txt")

print("Il y a " + str(nbOfWords) + " mots sans caractères spéciaux dans le texte.")
