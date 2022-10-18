text = input("Entrez du texte : ")

with open("output.txt", "w") as output:
    output.write(text)

with open("output.txt", "r") as output:
    print(output.read())