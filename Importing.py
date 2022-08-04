def enter():
    name = input("Enter the name of your dish: ")
    f = open("dishes.txt", "a")
    x = input("Enter your groceries: ").split()
    for line in range(len(x)):
           f.write(x[line]+" ")
    f.write(name+"\n")
    f.close()
    y = input("Enter the amount of groceries in grams: ").split()
    z = list(map(int, y))
    total = 0
    for line in range(len(z)):
        total += z[line]
    f = open("quantity.txt", "a")
    for line in range(len(y)):
           f.write(y[line]+" ")
    f.write(str(total)+"\n")
    f.close()