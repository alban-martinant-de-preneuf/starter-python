from importlib.machinery import FileFinder


def sayHelloTo(firstName, lastName):
    print("Bonjour {0} {1}.".format(firstName, lastName))

#test
#sayHelloTo("Ruben","Habib")