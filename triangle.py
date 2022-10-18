triangleHeight = int(input("Entrez la hauteur du triangle : "))

for i in range(0, triangleHeight):
    if i == 0:
        outsideSpaces = (triangleHeight - 1)
        insideSpaces = 0
    if i == triangleHeight - 1:
        insideChar = "_"
    else:
        insideChar = " "
    
    print( (outsideSpaces * " ") + "/" + (insideSpaces * insideChar) + "\\" )
    outsideSpaces -= 1
    insideSpaces += 2