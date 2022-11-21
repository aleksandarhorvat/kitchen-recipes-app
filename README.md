<h1 align="center">An application for keeping records of kitchen recipes</h1>
<p align="center">- term paper for the subject Script languages -</p>

# The content

1. [Introduction](#1-introduction)

2. [Description of the program](#2-description-of-the-program)

    2.1 [Main menu](#21-main-menu)

    2.2 [Registration](#22-registration)

    2.3 [Writing](#23-writing)

    2.4 [Reading](#24-reading)

    2.5 [Percentages](#25-percentages)

3. [Conclusion](#3-conclusion)

4. [Literature](#4-literature)

# 1. Introduction

We've all been in a situation where we have very random ingredients at our disposal and we don't know what to make with them, that's why this program was designed to help us choose dishes that we can make with the ingredients we currently have at home.

The application has one main file from which the program itself is launched and four more modules that are imported into the main file:

1. <ins>Registration:</ins> this module will enable the registration and login of users who want to use this application, it will use text files to store user registration data.
    ```
    alex mypass123
    peter something8
    ```
    > Lines within the text file login.txt

2. <ins>Writing:</ins> this module will allow users to enter ingredients and ingredient quantities into two separate text files, one of which will store the ingredients and the other the ingredient quantity.
    ```
    tomato cheese pepperoni pizza_dough pizza
    bread egg butter toast
    ```
    > Lines within the text file dishes.txt
    ```
    100 150 200 150 600
    300 100 50 450
    ```
    > Lines within the text file quantity.txt
    
3. <ins>Reading:</ins> this module will allow users to enter the ingredients they currently have with them, after that it will list all possible combinations with the given ingredients and allow the selection of all recipes that contain those ingredients and also list all other ingredients that we lack.

4. <ins>Percentages:</ins> this module will allow to convert the quantity of ingredients from grams to percentages which we will later need to display them graphically in the main module

# 2. Description of the program

The application is called from the main file Main.py, more precisely from the main() method. In this file, the corresponding modules are called first
``` Python
import matplotlib.pyplot as plt #is used for graphic display
from Percentages import percentage #used to convert grams to percentages
from Registration import check #is used for user registration and login
from Writing import enter #is used to enter foods and their quantities
from Reading import read #it is used to enter the ingredients that we have with us
                         #prints all possible combinations with the given ingredients
                         #enables the selection of all recipes that contain these ingredients
                         #it also lists all the other missing ingredients
import sys #we use it to exit the program
```
> Modules that are imported into the main file

## 2.1 Main menu

In the main() method, the check() method from the Registration.py module is first used. If that method returns True, then we continue with the program execution, and if it is returned False, then we first sign in and exit the program with sys.exit().

``` Python
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
```

> main() method

After that, a do-while loop is run to enter the choices.

If we chose 1, we first call the method read() from the Reading.py module, which returns a dictionary in which the key is the name of the dish and the value is a tuple with two lists, one containing the names of the ingredients and the other containing the amounts of the ingredients in grams.

![image](https://user-images.githubusercontent.com/108305750/182723098-a4e61f9f-dc2b-4e6c-9a5d-589befa6b215.png)
> Example of what the read() method returns

After that, we enter the desired dish and store its values in two lists, then transfer from string to int another list.

We convert values into percentages with the help of the percentage() method from the Percentages.py module, which receives a list to be changed as an argument.

Then we write down how much we need for each ingredient.

After that, we show a graph showing the percentage of each ingredient in the dish using the matplotlib.pyplot method.

If we did not choose 1 but 2 in the first choice, then the enter() method from the Writing.py module is executed.

And if we chose 3, then it jumps out of the loop and the program ends.

## 2.2 Registration

The module *Registration* is located in the file Registration.py, it is intended to sign in and log in users who want to use this application, it uses text files to save user registration data. There are 3 methods in this module:

1. signIn(): used for user registration that store it on a text file.

   ``` Python
   def signIn():
       print("\nSign in here")
       print("------------------------------------------------")
       username = input("Enter your username: ")
       password = input("Enter your password: ")
       f = open("login.txt", "a")
       f.write(username+" "+password+"\n")
       f.close()
   ```

   > singIn() method

2. logIn(): used to check if there is a matching username and password in the text file

   ``` Python
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
   ```

   > logIn() method

3. check(): used to check if the user has an account and if not create one

   ``` Python
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
   ```

   > check() method

## 2.3 Writing

The *Writing* module is located in the file Writing.py and is intended for entering ingredients and amounts of ingredients in two separate text files. There is one method in this module:

1. enter(): is used for the name of the dish, the ingredients needed for its preparation and their quantity in grams

   ``` Python
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
   ```

   > enter() method

## 2.4 Reading

The *Reading* module is located in the Reading.py file, it is intended for entering the ingredients that users currently have with them, after that it prints all possible combinations with the given ingredients and enables the selection of all recipes that contain those ingredients and also prints all other ingredients that we miss. There is one method in this module:

1. read(): it is used to obtain all the recipes from the text document, then it asks for input until only "Enter" is entered, after entering the ingredients we have with us, with the help of the imported method itertools.combinations(), all possible combinations are made from the possible entered ingredients and what can be made from them is printed, after that it returns a dictionary containing tuples with the data of all recipes

   ``` Python
   import itertools

   def read():
       f = open("dishes.txt", "r")
       recipes = []
       lines = f.readlines()
       for line in lines:
           temp = line.strip().split(" ")
           recipes.append((set(temp[:-1]),temp[-1]))
       f.close()
       query = input("Enter your groceries: ")
       available = query.strip().split(" ")
       for i in range(1, len(available)+1):
           for ingredients in itertools.combinations(available, i): #makes a tuple of size i from the list of available
               ingredient_set = set(ingredients)
               temp = True
               for recipe in recipes:
                   if ingredient_set <= recipe[0]:
                       if temp == True:
                           print("------------------------------------------------")
                           print("\n\nFor {} we can make:".format(" and ".join(ingredient_set)))
                           temp = False
                       print("------------------------------------------------")
                       print("Dish: {} \nIngredients: {}".format(recipe[1], ", ".join(recipe[0])))
       f = open("quantity.txt", "r")
       dictionary = dict()
       for i in range(len(recipes)):
           temp = (list(recipes[i][0]),f.readline().strip().split(" "))
           dictionary[recipes[i][1]]=temp
           temp = ()
       return dictionary
   ```

   > read() method

## 2.5 Percentages

The module *Percentages* located in the file Percentages.py is intended to convert the amount of ingredients from grams to percentages that we will need later to display them graphically in the main module. There is one method in this module:

1. percentage(): is used to convert values from grams to percentages and returns a new list

   ``` Python
   def percentage(temp):
       total = temp.pop(-1)
       for i in range(len(temp)):
           temp[i] = (temp[i] * 100)/total
       return temp
   ```

   > percentage() method

# 3. Conclusion

This application shows that with the help of programming it is possible to create applications that are not too demanding and can help in everyday life. In order to keep the application simple, the graphical interface and the entry of the recipes themselves have been omitted, which can be added later for a simpler work with the application itself.

# 4. Literature

Used literature:

1. Presentations from lectures
