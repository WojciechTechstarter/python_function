# A program which plays rock papaer scissor with the user

# Importing the right module

import random


# Creating the choices for the computer

options = ['Rock', 'Paper', 'Scissors']



def rps():
    user = input('Choose Rock, Paper or Scissors. ')  # User's choice
    print(f'You chose {user}.')

    computer = random.choice(options)               # Computer's choice
    print(f'Computer chose {computer}.')

    if user == computer:                            # Deciding who is the winner
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

