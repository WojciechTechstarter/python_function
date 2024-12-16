# Define a funktion 'square', which takes a number and multiples it by itself
#Definition of a funktion

def square(zahl):
    return pow(zahl, 0.5)

# return zahl * zahl

#Calling the funktion
#user input

user_input = float(input('Give me a number: '))


print(square(user_input))