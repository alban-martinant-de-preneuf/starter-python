from email.policy import default


while (str != "Au revoir"):
    str = input(">")

    match str:
        case "Bonjour":
            print("Bonjour à toi")
        case "Au revoir":
            pass
        case default:
            print(str)
        
