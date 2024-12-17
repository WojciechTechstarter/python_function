# Create a temperature converter using functions and conditional statements


def Celsius(value):
    return (value * 9/5 ) + 32

def Fahrennheit(value):
    return (value - 32) * 5/9



def calc_temp():
    conversion = input('Which conversion would you like to perform? Type (F to C) or (C to F): ')
    if conversion == 'C to F':
        value = float(input('Input a temperature in Ceclius: '))
        print(f'The temperature in Fahrenheit is: {(Celsius(value))}')

    elif conversion == 'F to C':
        value = float(input('Input a temperature in Fahrenheit: '))
        print(f'The temperature in Celcius is: {(Fahrennheit(value))}')

    else:
        print(f'Invalid version! Please type ´C to F´ or ´F to C´!')

calc_temp()
