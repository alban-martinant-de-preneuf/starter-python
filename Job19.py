def sortNumbersWithoutSort(*numbers):
    myList = list(numbers)

    swapped = True
    while swapped:
        #Si le programme n'entre pas dans le if on arrêtera le while 
        #car ça signifit que c'est déjà trié.
        swapped = False
        for i in range(0, len(myList) - 1):
            if myList[i + 1] < myList[i]:
                myList[i + 1], myList[i] = myList[i], myList[i + 1]
                #Si le programme est entré dans le if, on continue
                swapped = True

    print(myList)

#test :
#sortNumbersWithoutSort(4,64,9,54,47,6,15,7)