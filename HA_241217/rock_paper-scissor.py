# A program which plays rock papaer scissor with the user

# Importing the right module

import random

# Creating the choices for the computer

options = ['Rock', 'Paper', 'Scissors']

# Creating 3 variables for keeping the score


users_points = 0

computers_points = 0

draw = 0


  
                                                     
def rps():
        user = input('Choose Rock, Paper or Scissors. ')  # User's choice
        print(f'You chose {user}.')

        computer = random.choice(options)               # Computer's choice
        print(f'Computer chose {computer}.')

        if user == computer:                            # Deciding who is the winner
            print('It is a draw!')
            return 'draw'

        elif user == 'Rock' and computer == 'Scissors' or \
            user == 'Paper' and computer == 'Rock' or \
            user == 'Scissors' and computer == 'Paper':
            print('You Win!')
            return 'win'

        else: 
            print('You loose!')
            return 'loose'

rps()

while True:                                 # command to continue the game (look line 51)
    result = rps()                          # variable essenstial to add points according to the result

    if result == 'win':                      # adding the points
        users_points += 1
    elif result == 'loose':
        computers_points += 1
    else:
        draw += 1

    print(f'Game results: You {users_points}, Computer {computers_points}, Draw {draw}')  # displaying the points
        

    end_question = input('Would you like to contunue? Yes / No ')    # Continue the game
    if end_question != 'Yes':
        print('Thank you for the game!')
        break




    # Choosing the winner

