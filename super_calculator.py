# !!!!! SUPER POCKET CALCULATOR !!!!!

# Make a calculator, that is able to perform many task


############################################################## NOT DONE YET #############################################

# Function 1 - 4

def add(number_1, number_2):
    return number_1 + number_2

def subtract(number_1, number_2):
    return number_1 - number_2

def mult(number_1, number_2):
    return number_1 * number_2

def div(number_1, number_2):
    return number_1 / number_2

def area(length, width):
    return length * width
    

# Ask a user

def calculator():
    user_input = input('To add type  ')

    number_1 = float(input('Input the first number: '))
    number_2 = float(input('Input the second number: '))

    if user_input == 'add':
        print(f'{number_1} + {number_2} = {add(number_1, number_2)}')

    elif user_input == 'subtract':
        print(f'{number_1} - {number_2} = {subtract(number_1, number_2)}')

    elif user_input == 'mult':
        print(f'{number_1} * {number_2} = {mult(number_1, number_2)}')

    elif user_input == 'div':
        print(f'{number_1} / {number_2} = {div(number_1, number_2)}')
    else:
        print(f'Incorrect input! Type `add`, `subtract`, `mult` or `div`!')

calculator()