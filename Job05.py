value1 = int(input("Entrez la première valeur : "))
value2 = int(input("Entrez la deuxième valeur : "))

if value1 < value2:
    for i in range(value1 + 1, value2):
        print(i)
elif value1 > value2:
    for i in range(value1 - 1, value2, -1):
        print(i)
else:
    print("Valeurs égales")

    