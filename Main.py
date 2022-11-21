import matplotlib.pyplot as plt #is used for graphic display
from Percentages import percentage #used to convert grams to percentages
from Registration import check #is used for user registration and login
from Writing import enter #is used to enter foods and their quantities
from Reading import read #it is used to enter the ingredients that we have with us
                         #prints all possible combinations with the given ingredients
                         #enables the selection of all recipes that contain these ingredients
                         #it also lists all the other missing ingredients
import sys #we use it to exit the program

def main():
    answ = check()
    if answ == True:
        x = 1
        while x == 1 or x == 2:
            print("Please select: ")
            print("1) Check out our recipes")
            print("2) Enter your recipes")
            print("3) Exit the program")
            x = eval(input("Enter your selection: "))
            print("------------------------------------------------")
            if x == 1:
                choices = read()
                print("------------------------------------------------")
                choice = input("Enter your choice: ")
                print("------------------------------------------------")
                ingredients = choices[choice][0]
                quantity = choices[choice][1]
                quantity1 = [int(i) for i in quantity]
                quantity1 = percentage(quantity1)
                quantity.pop(-1)
                for i in range(0,len(quantity)):
                    print("For " + ingredients[i] + " you will need: " + quantity[i] + " grams")
                print("------------------------------------------------")
                fig1, ax1 = plt.subplots()
                ax1.pie(quantity1, labels=ingredients, autopct='%1.1f%%', shadow=True, startangle=90)
                plt.title(choice)
                ax1.axis('equal')
                plt.show()               
            elif x == 2:
                enter()
            else:
                continue
    else:
        sys.exit()
    
if __name__ == '__main__':
    main()