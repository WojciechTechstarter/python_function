# Calculate an are of a rectangle
def area(length, width):
    return length * width

def calc_area():
    length = float(input('Input the length of the rectangle: '))
    width = float(input('Input the width of the rectangle: '))
    print(f'The area of the rectangle is equal to {area(length, width)}')

calc_area()

# write a function which translates miles to kilometers

def m_to_k(miles):
    return miles * 1.60934

def miles_to_kilometers():
    miles = float(input('How many miles would you like to convert into kilometers? '))
    print(f'{miles} miles(s) equal(s) {m_to_k(miles)} kilometers')

miles_to_kilometers()

# write a function which translates kilometers to miles

def k_to_m(kilometers):
    return kilometers / 1.60934

def kilometers_to_miles():
    kilometers = float(input('How many kilometers would you like to convert into miles? '))
    print(f'{kilometers} kilometer(s) equal(s) {k_to_m(kilometers)} miles')

kilometers_to_miles()