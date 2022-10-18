width = int(input("Largeur : "))
height = int(input("Hauteur : "))

for i in range(0, height):
    display = "|"
    for j in range(0, width):
        if ( i == 0 or i == height - 1):
            display = display + "-"
        else:
            display = display + " "
    display = display + "|"
    print(display)
