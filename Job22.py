def charToUpper(char):
    corDict = {
        "a" : "A",
        "b" : "B",
        "c" : "C",
        "d" : "D",
        "e" : "E",
        "f" : "F",
        "g" : "G",
        "i" : "I",
        "j" : "J",
        "k" : "K",
        "l" : "L",
        "m" : "M",
        "n" : "N",
        "o" : "O",
        "p" : "P",
        "q" : "Q",
        "r" : "R",
        "s" : "S",
        "t" : "T",
        "u" : "U",
        "v" : "V",
        "w" : "W",
        "x" : "X",
        "y" : "Y",
        "z" : "Z"
    }
    if char in corDict:
        return corDict[char]
    else:
        return char


def charToLower(char):
    corDict = {
        "A" : "a",
        "B" : "b",
        "C" : "c",
        "D" : "d",
        "E" : "e",
        "F" : "f",
        "G" : "g",
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
    if char in corDict:
        return corDict[char]
    else:
        return char


def myUpper(str):
    newString = ""
    for char in str:
        newString += charToUpper(char)
    return newString


def myLower(str):
    newString = ""
    for char in str:
        newString += charToLower(char)
    return newString


def myTitle(str):
    words = []
    tmpWord = ""
    for char in str:
        if char != " ":
            tmpWord += char
        else:
            #Ajout du mot à la liste. Condition ternaire pour gérer les cas de mots à une lettre
            words.append(charToUpper(tmpWord[0]) + tmpWord[1:]) if len(tmpWord) > 1 else words.append(charToUpper(tmpWord))
            tmpWord = ""
    #Ajout du dernier mot
    words.append(charToUpper(tmpWord[0]) + tmpWord[1:]) if len(tmpWord) > 1 else words.append(charToUpper(tmpWord))
    newString = ""
    for word in words:
        newString += word + " "
    return newString


def myClean(str):
    newString = ""
    for char in str:
        if char == " ":
            newString += ""
        else:
            newString += char
    return newString
            

theString = input("Entrez une chaine de caractères : ")
treatment = input("Entrez traitement voulu (upper, lower, title ou clean) : ")

match treatment:
    case "upper":
        print(myUpper(theString))
    case "lower":
        print(myLower(theString))
    case "title":
        print(myTitle(theString))
    case "clean":
        print(myClean(theString))
    case default:
        print("Le traitement \"" + treatment + "\" n'existe pas !")
