def signIn():
    print("\nSign in here")
    print("------------------------------------------------")
    username = input("Enter your username: ")
    password = input("Enter your password: ")
    f = open("login.txt", "a")
    f.write(username+" "+password+"\n")
    f.close()

def logIn():
    print("\nLog in here")
    print("------------------------------------------------")
    username = input("Enter your username: ")
    password = input("Enter your password: ")
    f = open("login.txt", "r")
    for line in f.readlines():
        x, y = line.split(" ")
        if username == x and password == y[:-1]:
            z = True
            break
        else:
            z = False
    f.close()
    return z

def check():
    answ = input("Do you have an account (Y/N): ")
    if answ == "Y" or answ == "y":
        x = logIn()
        if x == True:
            print("\nYou have entered the correct username and password\n")
            print("------------------------------------------------")
            return True
        else:
            print("\nYou entered the wrong username and password\n")
            print("------------------------------------------------")
            return False
    else:
        signIn()