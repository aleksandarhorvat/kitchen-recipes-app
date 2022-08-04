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