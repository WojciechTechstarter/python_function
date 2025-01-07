#Write a code that asks a user for dishes and saves them afterwards

favourite_meal= []

for _ in range(3):
    user=input(f'Write your favourite meal: ')
    favourite_meal.append(user)
    print(f'My current list: {favourite_meal}')

for x in favourite_meal:
    print(f'My favourite meal is {x}')
