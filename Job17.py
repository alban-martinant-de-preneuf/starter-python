def printEvenNumbers(*numbers):
    myList = list(numbers)
    for number in myList:
        if ( number % 2 == 0 ):
            print(number)

#test
#printEvenNumbers(14,16,55,44,96,77,8,63)