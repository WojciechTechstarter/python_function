# !!!!! SUPER POCKET CALCULATOR !!!!!

# Make a calculator, that is able to perform many task

# Basic calculator calculations 

def add(number_1, number_2):
    return number_1 + number_2

def subtract(number_1, number_2):
    return number_1 - number_2

def mult(number_1, number_2):
    return number_1 * number_2

def div(number_1, number_2):
    return number_1 / number_2

def area(length, width):     # Area of a rectangle
    return length * width
    
def m_to_k(miles):          # m to km
    return miles * 1.60934

def k_to_m(kilometers):        # km to m
    return kilometers / 1.60934

def Celsius(value):            # C to F
    return (value * 9/5 ) + 32

def Fahrennheit(value):         # F to C
    return (value - 32) * 5/9


# Ask a user

def calculator():
    user_input = input('Input given number to perform a task: 1 - add, 2 - subtract, 3 - multiply, 4 - divide, 5 - calc area of a rectangle, 6 - convert miles to kilometers, 7 - convert kilometers to miles, 8 - convert C to F, 9 - convert F to C. ')

    if user_input == '1':
        number_1 = float(input('Input the first number: '))
        number_2 = float(input('Input the second number: '))
        print(f'{number_1} + {number_2} = {add(number_1, number_2)}')

    elif user_input == '2':
        number_1 = float(input('Input the first number: '))
        number_2 = float(input('Input the second number: '))
        print(f'{number_1} - {number_2} = {subtract(number_1, number_2)}')

    elif user_input == '3':
        number_1 = float(input('Input the first number: '))
        number_2 = float(input('Input the second number: '))
        print(f'{number_1} * {number_2} = {mult(number_1, number_2)}')

    elif user_input == '4':
        number_1 = float(input('Input the first number: '))
        number_2 = float(input('Input the second number: '))
        print(f'{number_1} / {number_2} = {div(number_1, number_2)}')

    elif user_input == '5':
         length = float(input('Input the length of the rectangle: '))
         width = float(input('Input the width of the rectangle: '))
         print(f'The area of the rectangle is equal to {area(length, width)}')

    elif user_input == '6':
         miles = float(input('How many miles would you like to convert into kilometers? '))
         print(f'{miles} miles(s) equal(s) {m_to_k(miles)} kilometers')

    elif user_input == '7':
         kilometers = float(input('How many kilometers would you like to convert into miles? '))
         print(f'{kilometers} kilometer(s) equal(s) {k_to_m(kilometers)} miles')

    elif user_input == '8':
         value = float(input('Input a temperature in Ceclius: '))
         print(f'The temperature in Fahrenheit is: {(Celsius(value))}')

    elif user_input == '9':
         value = float(input('Input a temperature in Fahrenheit: '))
         print(f'The temperature in Celcius is: {(Fahrennheit(value))}')

    else:
        print(f'Incorrect input! Type `add`, `subtract`, `mult` or `div`!')

calculator()


