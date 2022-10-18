def mySort(list):

    swapped = True
    while swapped:
        #Si le programme n'entre pas dans le if on arrêtera le while 
        #car ça signifit que c'est déjà trié.
        swapped = False
        for i in range(0, len(list) - 1):
            if list[i + 1] < list[i]:
                list[i + 1], list[i] = list[i], list[i + 1]
                #Si le programme est entré dans le if, on continue
                swapped = True

    return list

def myDisplay(list):
    print("Le contenu de la liste est :")
    for element in list:
        print(element)

#test :
#myDisplay(mySort([15,6,45,5,69,47,17]))