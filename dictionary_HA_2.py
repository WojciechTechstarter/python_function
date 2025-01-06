#1. Create a dictionary which translates 3 german words into english. 
#2. If there is no such word, make the user write the translation of it.
#3. With exit command, exit the loop and the program.


def translation(german_word):
    ger_eng = {'apfel':'appel', 'tor':'gate', 'hund':'dog'}

    if german_word in ger_eng:
        print(f'The translation of {german_word} is {ger_eng[user_input]}')
    else:
        actual_tranlation = input(f'This word is not in the dictionary. Please write an english translation: ')
        ger_eng[user_input] = actual_tranlation
        print(f'The translation of {user_input} is {ger_eng[user_input]}')


user_input = input(f'Write a german word: ').lower()
if  user_input == 'exit':
    print(f'I am not going to translate anything.')
else:
    translation(user_input)



