# Create a class that describes pets & more

class Pet:
    def __init__(self, name, species, age, favorite_food, energy_level):
        self.name = name
        self.species = species
        self.age = age
        self.favorite_food = favorite_food
        self.energy = energy_level

    # Method which describes the pets
    def get_description(self):
        return f'{self.name} is a {self.species} and is {self.age} years old'

    # Method which simulate the play duration and energy loss of pets
    def play(self, duration):
        self.energy = self.energy - (duration * 5)     # 1 minute is 5 points of energy
        if self.energy < 0:
            self.energy = 0

    # Method which feeds the pet. 30 points for the favorite food, 10 for other.
    def feed(self, food):
        if food == self.favorite_food:
            self.energy = self.energy + 30
        else:
            self.energy = self.energy + 10
        if self.energy > 100:
            self.energy = 100
        
    # Method which recovers the pets energy through sleep
    def sleep(self, hours):
        self.energy = self.energy + (hours * 20)
        if self.energy > 100:
            self.energy = 100

my_dog = Pet('Zak', 'dog', 6, 'sausage', 100)
my_cat = Pet('Fluffy', 'cat', 3, 'Whiskas', 100)

print(f'{my_dog.get_description()} \n{my_cat.get_description()}') 

my_dog.play(100)
my_cat.play(15)

print(f'{my_dog.name} has {my_dog.energy} energy left,\n{my_cat.name} has {my_cat.energy} energy left ')

my_cat.feed('Whiskas')

print(f'Mmmm {my_cat.name} loves Whiskas! He has now {my_cat.energy} energy left')

my_cat.feed('fish')

print(f'{my_cat.name} has eaten some fish! He has now {my_cat.energy} energy left')

my_cat.play(10)

print(f'{my_cat.name} has played for 10 minutes and has only {my_cat.energy} energy left!!!')

my_cat.sleep(3)

print(f'{my_cat.name} has has slept for 3 hours and has already {my_cat.energy} energy left :) ')