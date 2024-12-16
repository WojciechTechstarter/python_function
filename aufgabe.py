#Write a function, which asks the user for the age and shows it in the console

#def your_age():
#    age = int(input('Input your age: '))
#    print(f'You are {age} years old')

#your_age()

# 1.

def users_name():
    name = input('Input your name: ')
    print(f'Your name is {name}')

users_name()

# 2.

def users_name_2():
    name_2 = input('Input your name: ')
    return (f'Your name is {name_2}.')

print(users_name_2())

# 3.

def add(zahl1, zahl2):
    return zahl1 + zahl2

user_input = float(input('Input a number'))
