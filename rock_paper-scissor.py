# A program which plays rock papaer scissor with the user

# Importing the right module

import random


# Creating the choices for the computer

options = ['Rock', 'Paper', 'Scissors']

# User's choice


def rps():
    user = input('Choose Rock, Paper or Scissors. ')
    print(f'You chose {user}.')

    computer = random.choice(options)
    print(f'Computer chose {computer}.')

    if user == computer:
        print('It is a draw')

    elif user == 'Rock' and computer == 'Scissors' or \
         user == 'Paper' and computer == 'Rock' or \
         user == 'Scissors' and computer == 'Paper':
        print('You Win!')

    else: 
        print('You loose!')


rps()

# Computer's choice



# Choosing the winner

