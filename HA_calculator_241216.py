# !!!!! POCKET CALCULATOR !!!!!

#Schreibe zunächst 4 Funktionen: add(x,y), subtract(x,y), mult(x,y) und div(x,y)

# Function 1 - 4

def add(number_1, number_2):
    return number_1 + number_2

def subtract(number_1, number_2):
    return number_1 - number_2

def mult(number_1, number_2):
    return number_1 * number_2

def div(number_1, number_2):
    return number_1 / number_2

# Ask a user

def calculator():
    user_input = input('Would you like to add, subtract, mult or div? ')

    if user_input == 'add':
        number_1 = float(input('Input the first number: '))
        number_2 = float(input('Input the second number: '))
        print(add(number_1, number_2))

    elif user_input == 'subtract':
        number_1 = float(input('Input the first number: '))
        number_2 = float(input('Input the second number: '))
        print(subtract(number_1, number_2))

    elif user_input == 'mult':
        number_1 = float(input('Input the first number: '))
        number_2 = float(input('Input the second number: '))
        print(mult(number_1, number_2))

    elif user_input == 'div':
        number_1 = float(input('Input the first number: '))
        number_2 = float(input('Input the second number: '))
        print(div(number_1, number_2))
    else:
        print(f'Incorrect input! Type `add`, `subtract`, `mult` or `div`!')

calculator()