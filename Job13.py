import re

number = int(input("Entrez un nombre entier : "))

with open("data.txt") as data:
   findedWords = re.findall(r"\b[a-zA-Z]{%d}\b" %(number), data.read())

print("Il y a {0} mots de {1} lettres dans le texte.".format(len(findedWords), number))