#  Aufgabe 1

#Write a program that counts the number of certain letters in given text.


user_text = input(f'Write some text. ').lower()
user_letter = input(f'Choose a letter. ')

counter = 0
for x in user_text:                  # starting a loop (Schleife)
    if x == user_letter:             # comparing the letters
        counter +=1                  # adding +1 if they are the same




print(f'The number of letters {user_letter} in {user_text} is equal to {counter}.')


# Aufgabe 2

list_of_numbers = []

user_1 = float(input(f'Input the first number. '))
user_2 = float(input(f'Input the second number. '))
user_3 = float(input(f'Input the third number. '))
user_4 = float(input(f'Input the fourth number. '))
user_5 = float(input(f'Input the fifth number. '))

# append all at the same time not possible (in one line) ?
list_of_numbers.append(user_1)
list_of_numbers.append(user_2)
list_of_numbers.append(user_3)
list_of_numbers.append(user_4)
list_of_numbers.append(user_5)

print(list_of_numbers)

sum = 0
average = 0

for _ in list_of_numbers:
    sum += _
    
print(f'The sum = {sum}, the average = {sum/5}')



# Aufgabe 3

# Muster mit Schleifen erstellen (20 Punkte)
# Erstelle ein Muster mit einer verschachtelten Schleife. Beispiel:
# Der Benutzer gibt die Anzahl der Zeilen ein, und das Programm gibt folgendes Muster aus.

# Ask the user to input the number of rows
number_of_rows = int(input("Enter the number of rows: "))

# Outer loop: controls the number of rows
for i in range(1, number_of_rows + 1):  # Starts from 1 and goes up to 'number_of_rows'
    # Inner loop: prints the correct number of asterisks for the current row
    for j in range(i):  # 'i' determines how many stars to print in the current row
        print("*", end="")  # Print an asterisk without moving to a new line
    print()  # Moves to the next line after printing all asterisks in the current row
