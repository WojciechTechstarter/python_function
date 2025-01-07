
# creating a class ingredient
class ingredient():
    # here is a contructor which shows the basic attributes of the class
    def __init__(self, name: str, calories: int, preperation_time: int):
        self.name = name
        self.calories_pro_100g = calories
        self.preparation_time = preperation_time

        
# Let's test it !

potato = ingredient('potato', 77, 30)   # adding ingredients to the class (ingridients + attributes)

# Cheking if works

print(potato.name)                                          # potato
print(potato.calories_pro_100g, potato.preparation_time)    # 77 30 



# creating another class - recipe

class recipe():
    def __init__(self, name: str, description: str,):   # don't add type dictionary here
        self.name = name
        self.description = description
# here's a dictionary first introduced (as a key, it doesn't have a str, but object ours ingridients list )
        self.list_of_ingridients = {}      


# Adding the method which adds ingridients to list of ingridients

    def add_ingridient(ingredient):
        