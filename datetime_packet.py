
# importing the date time module, together with 

from datetime import datetime, date

# 1. Show the actual time and date

actual_date_and_time = datetime.now()
print('Right now is:', actual_date_and_time.strftime('%d.%m.%y %H:%M:%S'))


# 2. Show difference until the end of the year - 31th of December 2024

today = date.today()   # Today's date



def days_until_end_year():
    today = date.today()                                      #today's date
    end_of_the_year = date(today.year, 12, 31)             # Last day of the year
    days_until_end_year = end_of_the_year - today                  # The difference
    return days_until_end_year.days

print('Days until the end of the year:', days_until_end_year())  



# 3 Function that calculates number of days between the current date and the one given by user



def days_until_date():
    while True:                                                 # loop regarding the correct date
        
        user_input = input(f'Input a date as follows DD.MM.YYYY')
        try:
            # converting the user's input into a date object
            user_date = datetime.strptime(user_input, '%d.%m.%y').date()                                              
            break
        except ValueError:
            print('Invalid format! Please enter the date as DD.MM.YYYY')

            # Today's date
        today = date.today()
            # Giving the difference back

        
        difference = user_input - today
        return difference.days




########  I tried to to it with ChatGPT and was on the right track, but didn't have enough time to continue. 
########  Looking forward to doing it all together during class :)