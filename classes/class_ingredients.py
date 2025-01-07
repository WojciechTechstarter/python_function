
# creating a class ingredient

class ingredient():
    # here is a contructor which shows the basic attributes of the class
    def __init__(self, name: str, calories: int, preperation_time: int):
        self.name = name
        self.calories_pro_100g = calories
        self.preparation_time = preperation_time

        
# Testing the ingredient class

potato = ingredient('potato', 77, 30)   # adding ingredients to the class (ingridients + attributes)


print(potato.name)                                          # potato
print(potato.calories_pro_100g, potato.preparation_time)    # 77 30 

# ---------------------------------

# creating another class - recipe with dictionary type inside

class recipe():
    def __init__(self, name: str, description: str,):   # don't add type dictionary here
        self.name = name
        self.description = description
# here's a dictionary first introduced (as a key, it doesn't have a str, but ?an object ours ingredient class? (line 4) )
        self.list_of_ingridients = {}      

# ----------------------------------

# adding a method that adds ingredient and its quantity to the recipe:
    def add_ingredient(self, ingredient: ingredient, quantity: str):
# adding the ingredient object as a key and the quantity as a value in the dictionary:
        self.list_of_ingridients[ingredient] = quantity

# Testing the recipe class 
# potato soup

recipe_1 = recipe('Potato soup', 'A tasty soup mainly made out of potatoes')

# Adding ingredients

recipe_1.add_ingredient(potato, '300g')

# Test
print(recipe_1.name, recipe_1.description)
# in order to print a whole dictionary we need a loop, that calls both the key and its value

for ingredient, quantity in recipe.list_of_ingredients.items():
    print()


#  I stop here, seems a little complicated for now. I definetly got something out of it,
#  but many questions appear and I did it mostly with the help of ChatGPT (which is fine, helped alot to understand some things).